# pylint: disable=no-member

import pynecone as pc


def saving_simulation() -> pc.Component:
    # questions: dict = {
    #     "Q1": ["What is saving?", "A", "B", "C", "D"],
    #     "Q2": ["Do you think saving money is important?", "No", "Maybe", "Yes"],
    # }
    # q1 = questions["Q1"][0]
    # ans1 = questions["Q1"][1:]

    # q2 = questions["Q2"][0]
    # ans2 = questions["Q2"][1:]

    return pc.center(
        pc.text("What would you do?"),
    )
