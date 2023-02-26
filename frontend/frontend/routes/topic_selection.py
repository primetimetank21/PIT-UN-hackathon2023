# pylint: disable=no-member

import pynecone as pc


class TopicSelectionState(pc.State):
    pass


def topic_selection() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.text("Topic Selection"),
            pc.link(
                pc.button("Next", color_scheme="green"),
                href="/initial-question",
                button=True,
            ),
        )
    )
