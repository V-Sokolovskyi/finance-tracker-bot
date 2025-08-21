from aiogram.fsm.state import StatesGroup, State
class AddTx(StatesGroup):
    waiting_for_amount = State()
    waiting_for_category = State()
    waiting_for_note = State()