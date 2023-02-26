# pylint: disable=no-member

import pynecone as pc


def topic_selection() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.text("Hello Timmy! What would you like to learn about?"),
            # Fin Lit Topics
            pc.button_group(
                pc.vstack(
                    pc.hstack(
                        pc.button(
                            "Budgeting",
                            bg="lightgreen",
                            color_scheme="green",
                            is_full_width=True,
                            color="black",
                            size="md",
                        ),
                        pc.link(
                            pc.button(
                                "Saving",
                                bg="lightgreen",
                                color_scheme="green",
                                is_full_width=True,
                                color="black",
                                size="md",
                            ),
                            href="/initial-question",
                            button=True,
                        ),
                    ),
                    pc.hstack(
                        pc.button(
                            "Earning",
                            bg="lightgreen",
                            color_scheme="green",
                            is_full_width=True,
                            color="black",
                            size="md",
                        ),
                        pc.button(
                            "Spending",
                            bg="lightgreen",
                            color_scheme="green",
                            is_full_width=True,
                            color="black",
                            size="md",
                        ),
                    ),
                    pc.hstack(
                        pc.button(
                            "Debt",
                            bg="lightgreen",
                            color_scheme="green",
                            is_full_width=True,
                            color="black",
                            size="md",
                        ),
                        pc.button(
                            "Investing",
                            bg="lightgreen",
                            color_scheme="green",
                            is_full_width=True,
                            color="black",
                            size="md",
                        ),
                    ),
                )
            ),
        )
    )
