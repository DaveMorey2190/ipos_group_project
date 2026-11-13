"""
notifications.py

Observer Pattern:
Allows multiple subscribers to receive notifications
when a document is uploaded.
"""

import logging

logger = logging.getLogger(__name__)


class UploadNotifier:
    """Manages subscribers and document upload notifications."""

    def __init__(self):
        # List of functions subscribed to upload events.
        self._subscribers = []

    def subscribe(self, callback):
        """Register a function to receive notifications."""

        if not callable(callback):
            raise TypeError("Subscriber must be callable")

        if callback not in self._subscribers:
            self._subscribers.append(callback)

    def unsubscribe(self, callback):
        """Remove a function from the subscriber list."""

        if callback in self._subscribers:
            self._subscribers.remove(callback)

    def notify(self, document):
        """Notify all subscribers that a document was uploaded."""

        for callback in self._subscribers.copy():
            try:
                callback(document)

            except Exception:
                # Continue notifying other subscribers
                # even if one subscriber fails.
                logger.exception(
                    "Error notifying subscriber: %s",
                    callback.__name__
                )