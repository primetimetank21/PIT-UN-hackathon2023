# pylint: disable=no-member

import pynecone as pc


def initial_question() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.text("Do you know what saving is?"),
            pc.button_group(
                pc.link(
                    pc.button(
                        "Yes",
                        bg="lightgreen",
                        color_scheme="green",
                        is_full_width=True,
                        color="black",
                        size="md",
                    ),
                    href="/questionnaire",
                    button=True,
                ),
                pc.link(
                    pc.button(
                        "No",
                        bg="red",
                        color_scheme="red",
                        is_full_width=True,
                        color="black",
                        size="md",
                    ),
                    href="/recommendations",
                    button=True,
                ),
            ),
        )
    )
