from fastapi import APIRouter

from app.models.schemas import ConversationRequest, ConversationResponse,Feedback
from app.services.event_analyzer import analyze_event
from app.services.topic_generator import generate_topics
from app.services.fact_checker import check_facts
from app.services.history_logger import save_history,get_history
from app.services.feedback_logger import save_feedback, get_feedback
from app.services.networking_tips import generate_networking_tips
from app.services.self_introduction import generate_self_introduction
from app.services.conversation_starters import generate_conversation_starters

router=APIRouter()

@router.post("/analyze-event")
def analyze_event_api(request: ConversationRequest):
    event_info = analyze_event(request.event)
    return event_info

@router.post("/fact-check")
def fact_check_api(request: ConversationRequest):
    topics = generate_topics(request.event)
    verified = check_facts(topics)
    return verified

@router.post("/feedback")
def submit_feedback(request: Feedback):
    save_feedback(request.user_name, request.feedback)
    return {"message": "Feedback saved successfully"}

@router.get("/feedback-history")
def feedback_history():
    return get_feedback()

@router.post("/generate-conversation",response_model=ConversationResponse)
    
def generate_conversation(request:ConversationRequest):
    event_info=analyze_event(request.event)
    topics=generate_topics(request.event)
    tips = generate_networking_tips(request.user, request.event)
    intro = generate_self_introduction(request.user, request.event)
    starters = generate_conversation_starters(request.user, request.event)
    verified=check_facts(topics)

    save_history(
        request.user.name,
        request.event.title,
        topics
    )
    history = get_history()


    return ConversationResponse(
        suggested_topics=verified["verified_topics"],
        networking_tips=tips,
        self_introduction=intro,
        conversation_starters=starters,
        history=history,
        fact_check_status=verified["status"]
    )

