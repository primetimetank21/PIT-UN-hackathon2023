# pylint: disable=no-member

import pynecone as pc


def saving_simulation() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.text("What would you do?", font_size="3em"),
            pc.text("You have $10", font_size="2em"),
            pc.text("🍔 is $6", font_size="1em"),
            pc.text("🍭 is $4", font_size="1em"),
            pc.text("Choose what you want to buy:", font_size="2em"),
            pc.hstack(
                pc.button_group(
                    pc.link(
                        pc.button(pc.text("🍔", font_size="1.5em"), size="lg"),
                        href="/saving-simulation-burger",
                        button=True,
                    ),
                    pc.link(
                        pc.button(pc.text("🍭", font_size="1.5em"), size="lg"),
                        href="/saving-simulation-candy",
                        button=True,
                    ),
                )
            ),
        )
    )
