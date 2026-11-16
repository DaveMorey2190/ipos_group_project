


"""
logging_utils.py

Decorator Pattern:
Automatically records user actions
performed within the document management system.
"""

import logging
from functools import wraps


# Configure application logging.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def action_logger(func):
    """Decorator that records user actions."""

    @wraps(func)
    def wrapper(*args, **kwargs):

        # Find the user object in the function arguments.
        user = kwargs.get("user")

        if user is None:
            for argument in args:
                if (
                    hasattr(argument, "name")
                    and hasattr(argument, "get_role")
                ):
                    user = argument
                    break

        # Identify the user performing the action.
        if user is not None:
            username = user.name
            role = user.get_role()
            actor = f"{username} ({role})"
        else:
            actor = "Unknown user"

        # Get the name of the original function.
        action = func.__name__

        try:
            # Execute the original function.
            result = func(*args, **kwargs)

            # Record successful action.
            logger.info(
                "%s performed action: %s",
                actor,
                action
            )

            return result

        except Exception:
            # Record unsuccessful action.
            logger.exception(
                "%s failed during action: %s",
                actor,
                action
            )

            raise

    return wrapper