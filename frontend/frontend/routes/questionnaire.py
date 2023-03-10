# pylint: disable=no-member

import pynecone as pc


def questionnaire() -> pc.Component:
    questions: dict = {
        "Q1": ["How much of your money do you save?", "None", "Some", "Almost all"],
        "Q2": ["Do you think saving money is important?", "No", "Maybe", "Yes"],
    }
    q1 = questions["Q1"][0]
    ans1 = questions["Q1"][1:]

    q2 = questions["Q2"][0]
    ans2 = questions["Q2"][1:]

    return pc.center(
        pc.vstack(
            pc.text("Saving Questionnaire", font_size="3em"),
            pc.text(q1, font_size="2em"),
            pc.hstack(
                *[
                    pc.button(
                        option,
                        bg="lightgreen",
                        color_scheme="green",
                        is_full_width=True,
                        color="black",
                        size="md",
                    )
                    for option in ans1
                ]
            ),
            pc.text(q2, font_size="2em"),
            pc.hstack(
                *[
                    pc.button(
                        option,
                        bg="lightgreen",
                        color_scheme="green",
                        is_full_width=True,
                        color="black",
                        size="md",
                    )
                    for option in ans2
                ]
            ),
            pc.link(
                pc.button("Next", color_scheme="green"),
                href="/recommendation-higher",
                button=True,
            ),
        )
    )
