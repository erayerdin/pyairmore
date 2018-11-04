"""This package contains services to help developers access Airmore server.

Services represent different aspects of Airmore server.
"""

import pyairmore.request


class Service:
    """Service represents an aspect of Airmore, like messages, contacts and
    gallery, each is an aspect and has their services.

    This class is used to extend these aspects. You are likely to use this
    class if you plan to develop/extend the library. If you utilize the
    library, then you need to use other implementations, which are in their
    own modules.

    **Instance Attributes**
     - **session: pyairmore.request.AirmoreSession** -- Parent session.
    """

    def __init__(self, session: pyairmore.request.AirmoreSession):
        """
        :param session: Session to wrap.
        """

        self.session = session
