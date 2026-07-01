from fastapi import APIRouter

from app.models.schemas import ConversationRequest, ConversationResponse
from app.services.event_analyzer import analyze_event
from app.services.topic_generator import generate_topics
from app.services.fact_checker import check_facts
from app.services.history_logger import save_history
from app.services.feedback_logger import save_feedback

router=APIRouter()