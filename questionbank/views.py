from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Question
from .forms import QuestionForm

# List all questions
def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, "questionbank/home.html", {"questions": questions})

# Add a new question
@login_required
def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("questionbank_home")
    else:
        form = QuestionForm()
    return render(request, "questionbank/add_question.html", {"form": form})

# View a single question
def view_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, "questionbank/view_question.html", {"question": question})

# Download all questions as TXT
def download_txt(request):
    questions = Question.objects.all()
    content = ""
    for q in questions:
        content += f"Q: {q.question_text}\nA: {q.answer_text}\n\n"

    response = HttpResponse(content, content_type="text/plain")
    response['Content-Disposition'] = 'attachment; filename="question_bank.txt"'
    return response
