# pylint: disable=no-member

import pynecone as pc


def saving_simulation_burger() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.text("What would you do?", font_size="3em"),
            pc.text("You had $10", font_size="2em"),
            pc.text("🍔 is $6", font_size="1em"),
            pc.text("🍭 is $4", font_size="1em"),
            pc.text("Choose what you want to buy:", font_size="2em"),
            pc.hstack(
                pc.button_group(
                    pc.button(
                        pc.text("🍔", font_size="1.5em"), size="lg", is_disabled=True
                    ),
                    pc.button(
                        pc.text("🍭", font_size="1.5em"),
                        size="lg",
                    ),
                )
            ),
            pc.text("You spent $6", font_size="1.5em"),
            pc.text("You saved $4", font_size="1.5em"),
            pc.link(
                pc.button("Done", color_scheme="green"),
                href="/topic-selection",
                button=True,
            ),
        )
    )
