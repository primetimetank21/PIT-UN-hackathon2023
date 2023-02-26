# pylint: disable=no-member

import pynecone as pc


def recommendation_higher() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.text("What is Saving?", font_size="3em"),
            pc.text(
                "Watch the video below to learn more about saving", font_size="1.5em"
            ),
            pc.link(
                pc.image(src="/what_is_saving.png", width="50em", height="auto"),
                href="https://www.youtube.com/watch?v=wXHQjScKPzc&feature=youtu.be",
            ),
            pc.link(
                pc.button("Done", color_scheme="green"),
                href="/topic-selection",
                button=True,
            ),
        )
    )
