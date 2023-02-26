# pylint: disable=no-member

import pynecone as pc


class RecommendationsState(pc.State):
    pass


def recommendations() -> pc.Component:
    return pc.center(pc.text("Recommendations Page"))
