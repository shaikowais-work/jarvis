from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.conf import settings
from openai import OpenAI

@api_view(["POST"])
@permission_classes([IsAuthenticated])  # require login
def ask_ai(request):
    prompt = request.data.get("prompt", "").strip()
    if not prompt:
        return Response({"error": "prompt is required"}, status=400)

    api_key = settings.OPENAI_API_KEY
    if not api_key:
        return Response({"error": "OpenAI key not configured"}, status=500)

    client = OpenAI(api_key=api_key)
    # Simple, concise completion
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"Be concise and clear."},
            {"role":"user","content":prompt},
        ],
        temperature=0.4,
        max_tokens=300
    )
    answer = completion.choices[0].message.content
    return Response({"answer": answer})
