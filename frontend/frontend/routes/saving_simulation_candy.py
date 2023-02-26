# pylint: disable=no-member

import pynecone as pc


class TmpState(pc.State):
    show: bool = False
    piggybank: int = 10

    def add_to_bank(self, amount):
        self.piggybank += amount

    def toggle_show(self):
        self.show = not self.show

    def buy_candy(self):
        self.piggy -= 4

    def buy_burger(self):
        self.piggy -= 6


def saving_simulation_candy() -> pc.Component:
    state = TmpState()
    print(state.piggybank)

    return pc.center(
        pc.vstack(
            pc.text("What would you do?", font_size="3em"),
            pc.text("You had $10", font_size="2em"),
            pc.text("🍔 is $6", font_size="1em"),
            pc.text("🍭 is $4", font_size="1em"),
            pc.text("Choose what you want to buy:", font_size="2em"),
            pc.hstack(
                pc.button_group(
                    pc.button(pc.text("🍔", font_size="1.5em"), size="lg"),
                    pc.button(
                        pc.text("🍭", font_size="1.5em"), size="lg", is_disabled=True
                    ),
                )
            ),
            pc.text("You spent $4", font_size="1.5em"),
            pc.text("You saved $6", font_size="1.5em"),
            pc.link(
                pc.button("Done", color_scheme="green"),
                href="/topic-selection",
                button=True,
            ),
        )
    )
