import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.encoder import EncoderHandler

keyboard = KMKKeyboard()

# GPIO setup from schematic
keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4,
    board.GP5, board.GP6, board.GP7, board.GP8, board.GP9,
    board.GP10, board.GP11, board.GP12, board.GP13, board.GP14,  # Column 15 = GP14
)

keyboard.row_pins = (
    board.GP21,  # Row 1
    board.GP20,  # Row 2
    board.GP19,  # Row 3
    board.GP18,  # Row 4
    board.GP17,  # Row 5
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# --- Encoder Setup ---
encoder_handler = EncoderHandler()
keyboard.extensions.append(encoder_handler)

# ENCA = GP27, ENCB = GP26
encoder_handler.rotary_encoder_pins = ((board.GP27, board.GP26),)
encoder_handler.rotary_encoder_map = (((KC.VOLU, KC.VOLD),),)

# --- Keymap Definition (5 rows x 15 columns) ---
keyboard.keymap = [
    [  # Layer 0
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC, KC.MUTE,  # Row 1
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, KC.DEL,   # Row 2
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.NO,   KC.NO,    # Row 3
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.UP,   KC.NO,   KC.NO,    # Row 4
        KC.LCTL, KC.LGUI, KC.LALT, KC.NO,   KC.NO,   KC.SPC,  KC.NO,   KC.NO,   KC.NO,   KC.RALT, KC.FN0,  KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT,  # Row 5
    ]
]

if __name__ == '__main__':
    keyboard.go()
