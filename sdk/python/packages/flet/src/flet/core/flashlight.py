from typing import Any, Optional

from flet.core.control import Control
from flet.core.ref import Ref


class Flashlight(Control):
    """
    A control to use FlashLight. Works on iOS and Android. Based on torch_light Flutter widget (https://pub.dev/packages/torch_light).

    Flashlight control is non-visual and should be added to `page.overlay` list.

    Example:
    ```
    import flet as ft

    def main(page: ft.Page):
        flashLight = ft.Flashlight()
        page.overlay.append(flashLight)
        page.add(
            ft.TextButton("toggle", on_click: lambda _: flashlight.toggle())
        )

    ft.app(target=main)
    ```

    """

    def __init__(
        self,
        ref: Optional[Ref] = None,
        data: Any = None,
    ):
        Control.__init__(
            self,
            ref=ref,
            data=data,
        )

        self.turned_on = False

    def _get_control_name(self):
        return "flashlight"

    def _toggle_state(self, sr: str, on: bool=True) -> bool:
        self.turned_on = on if ("1" == sr) else self.turned_on
        return self.turned_on

    def turn_on(self, wait_timeout: Optional[int] = 5) -> bool:
        sr = self.invoke_method("on", wait_for_result=True, wait_timeout=wait_timeout)
        return self._toggle_state(sr)


    async def turn_on_async(self, wait_timeout: Optional[int] = 5) -> bool:
        sr = await self.invoke_method_async(
            "on", wait_for_result=True, wait_timeout=wait_timeout
        )
        return self._toggle_state(sr)


    def turn_off(self, wait_timeout: Optional[int] = 5) -> bool:
        sr = self.invoke_method("off", wait_for_result=True, wait_timeout=wait_timeout)
        return self._toggle_state(sr, False)
        

    async def turn_off_async(self, wait_timeout: Optional[int] = 5) -> bool:
        sr = await self.invoke_method_async(
            "off", wait_for_result=True, wait_timeout=wait_timeout
        )
        return self._toggle_state(sr, False)

    
    def toggle(self, wait_timeout: Optional[int] = 5) -> bool:
        _func = self.turn_off if self.turned_on else self.turn_on
        return _func(wait_timeout)

    
    async def toggle_async(self, wait_timeout: Optional[int] = 5) -> bool:
        if self.turned_on:
            return await self.turn_off_async(wait_timeout)
        return await self.turn_on_async(wait_timeout)
