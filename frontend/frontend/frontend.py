# pylint: disable=no-member
import pynecone as pc
from .routes.topic_selection import topic_selection
from .routes.initial_question import initial_question

# Component docs: https://pynecone.io/docs/library


class IndexState(pc.State):
    count: int = 0
    user_name: str = ""
    pass_word: str = ""

    def set_username(self, text):
        self.user_name = text

    def set_password(self, text):
        self.pass_word = text


def index():
    return pc.center(
        pc.vstack(
            pc.text("Sign in"),
            pc.avatar(name="John Doe"),
            # Username input
            pc.text("Username"),
            pc.input(
                placeholder="Username",
                on_blur=IndexState.set_username,
            ),
            # Password input
            pc.text("Password"),
            pc.password(
                placeholder="Password", on_blur=IndexState.set_password, hidden=True
            ),
            # Login button
            # pc.link(
            #         "Sign in",
            #         href="/topic_selection",
            #         border="0.1em solid",
            #         padding="0.5em",
            #         border_radius="0.5em",
            #         _hover={
            #             "color": "rgb(107,99,246)",
            #         },
            #     ),
            pc.link(
                pc.button("Sign in", color_scheme="green"),
                href="/topic-selection",
                button=True,
            ),
        ),
    )


app = pc.App(state=IndexState)
app.add_page(index, route="/")
app.add_page(topic_selection, route="/topic-selection")
app.add_page(initial_question, route="/initial-question")
app.compile()
