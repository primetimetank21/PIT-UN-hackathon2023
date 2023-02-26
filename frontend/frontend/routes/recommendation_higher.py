# pylint: disable=no-member

import pynecone as pc


class RecommendationsState(pc.State):
    pass


def recommendation_higher() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.text("What is Saving?"),
            pc.text("Watch the video below to learn more about saving"),
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


# https://miro.com/app/board/uXjVPjC5Enw=/?moveToWidget=3458764547251009381&cot=14
