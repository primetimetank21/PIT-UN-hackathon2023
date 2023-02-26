# pylint: disable=no-member

import pynecone as pc


def recommendations() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.text("What is Saving?", font_size="3em"),
            pc.text("Watch the video below to learn about saving", font_size="1.5em"),
            pc.link(
                pc.image(
                    src="/savings_goals_for_kids.png", width="50em", height="auto"
                ),
                href="https://www.youtube.com/watch?v=v-mlEQ7KW5Q",
            ),
            pc.link(
                pc.button("Next", color_scheme="green"),
                href="/progress-check",
                button=True,
            ),
        )
    )
