#
# pyimpi
#
# author: Heiko Thiery <heiko.thiery@kontron.com>
# author: Michael Walle <michael.walle@kontron.com>
#

from functools import partial

from pyipmi.errors import DecodingError, CompletionCodeError
from pyipmi.msgs import chassis as msgs
from utils import check_completion_code

from pyipmi.msgs.chassis import \
        CONTROL_POWER_DOWN, CONTROL_POWER_UP, CONTROL_POWER_CYCLE, \
        CONTROL_HARD_RESET, CONTROL_DIAGNOSTIC_INTERRUPT, \
        CONTROL_SOFT_SHUTDOWN

class Chassis:
    def chassis_control(self, option):
        m = msgs.ChassisControl()
        m.req.control.option = option
        self.send_message(m)
        check_completion_code(m.rsp.completion_code)

    def chassis_control_power_down(self):
        self.chassis_control(CONTROL_POWER_DOWN)

    def chassis_control_power_up(self):
        self.chassis_control(CONTROL_POWER_UP)

    def chassis_control_power_cycle(self):
        self.chassis_control(CONTROL_POWER_CYCLE)

    def chassis_control_hard_reset(self):
        self.chassis_control(CONTROL_HARD_RESET)

    def chassis_control_diagnostic_interrupt(self):
        self.chassis_control(CONTROL_DIAGNOSTIC_INTERRUPT)

    def chassis_control_soft_shutdown(self):
        self.chassis_control(CONTROL_SOFT_SHUTDOWN)
