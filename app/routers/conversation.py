from fastapi import APIRouter

from app.models.schemas import ConversationRequest, ConversationResponse
from app.services.event_analyzer import analyze_event
from app.services.topic_generator import generate_topics
from app.services.fact_checker import check_facts
from app.services.history_logger import save_history
from app.services.feedback_logger import save_feedback
from app.services.networking_tips import generate_networking_tips
from app.services.self_introduction import generate_self_introduction

router=APIRouter()

@router.post("/generate",response_model=ConversationResponse)
def generate_conversation(request:ConversationRequest):
    event_info=analyze_event(request.event)
    topics=generate_topics(request.event)
    tips = generate_networking_tips(request.user, request.event)
    verified=check_facts(topics)

    save_history(
        request.user.name,
        request.event.title,
        topics
    )

    return ConversationResponse(
    suggested_topics=verified["verified_topics"],
    networking_tips=tips,
    fact_check_status=verified["status"]
)

