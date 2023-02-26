# pylint: disable=no-member
import pynecone as pc
from .routes.initial_question import initial_question
from .routes.progress_check import progress_check
from .routes.questionnaire import questionnaire
from .routes.recommendation_higher import recommendation_higher
from .routes.recommendations import recommendations
from .routes.saving_simulation_burger import saving_simulation_burger
from .routes.saving_simulation_candy import saving_simulation_candy

from .routes.saving_simulation import saving_simulation
from .routes.topic_selection import topic_selection

# Component docs: https://pynecone.io/docs/library
# https://miro.com/app/board/uXjVPjC5Enw=/?userEmail=earl.tankard@bison.howard.edu&shareBoard=marcus.syrr@gmail.com&track=true&invite_entry_point=board&flow_feature=access_board&flow_type=request


class IndexState(pc.State):
    count: int = 0
    user_name: str = ""
    pass_word: str = ""
    show: bool = False
    piggybank: int = 10

    def set_username(self, text):
        self.user_name = text

    def set_password(self, text):
        self.pass_word = text

    def toggle_show(self):
        self.show = not self.show

    def buy_candy(self):
        self.piggy -= 4

    def buy_burger(self):
        self.piggy -= 6


def index():
    return pc.center(
        pc.vstack(
            pc.text("Sign in", font_size="3em"),
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
            pc.link(
                pc.button("Sign in", color_scheme="green"),
                href="/topic-selection",
                button=True,
            ),
        ),
    )


app = pc.App(state=IndexState)
app.add_page(index, route="/")
app.add_page(initial_question, route="/initial-question")
app.add_page(progress_check, route="/progress-check")
app.add_page(questionnaire, route="/questionnaire")
app.add_page(recommendation_higher, route="/recommendation-higher")
app.add_page(recommendations, route="/recommendations")
app.add_page(saving_simulation_burger, route="/saving-simulation-burger")
app.add_page(saving_simulation_candy, route="/saving-simulation-candy")
app.add_page(saving_simulation, route="/saving-simulation")
app.add_page(topic_selection, route="/topic-selection")
app.compile()
