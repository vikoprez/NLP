from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import pipeline

# Initialize the text generation pipeline
generator = pipeline("text-generation", model="ltphuong/my_awesome_eli5_clm-model")

def index(request):
    return render(request, 'index.html')

@api_view(['POST'])
def generate_text(request):
    prompt = request.data.get('prompt')
    if prompt:
        # Generate text using the language model
        result = generator(prompt)
        return Response(result[0]['generated_text'])
    else:
        return Response({'error': 'No prompt provided'}, status=400)
