from enum import Enum


# The values should be the same as the prompt file names
class RoleType(Enum):
    ASSISTANT = "assistant"
    USER = "user"
    DEFAULT = "default"


class ModelType(Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_4 = "gpt-4"
    GPT_4_32k = "gpt-4-32k"


# The values should be the same as the prompt dir names
class TaskType(Enum):
    AI_SOCIETY = "ai_society"
    CODE = "code"
    MISALIGNMENT = "misalignment"
    TRANSLATION = "translation"
    DEFAULT = "default"


__all__ = ['RoleType', 'ModelType', 'TaskType']
