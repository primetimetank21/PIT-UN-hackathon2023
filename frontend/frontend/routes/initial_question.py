# pylint: disable=no-member

import pynecone as pc


class InitialQuestionState(pc.State):
    pass


def initial_question() -> pc.Component:
    return pc.center(pc.vstack(pc.text("Initial Question")))
