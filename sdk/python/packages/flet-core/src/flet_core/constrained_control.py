from typing import Any, Optional, Union

from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import (
    AnimationValue,
    OffsetValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
    OptionalEventCallable,
    OptionalControlEventCallable,
)


class ConstrainedControl(Control):
    def __init__(
        self,
        ref: Optional[Ref] = None,
        expand: Union[None, bool, int] = None,
        expand_loose: Optional[bool] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
        rtl: Optional[bool] = None,
        #
        # ConstrainedControl specific
        #
        key: Optional[str] = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        aspect_ratio: OptionalNumber = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        on_animation_end: OptionalEventCallable = None,
    ):
        Control.__init__(
            self,
            ref=ref,
            expand=expand,
            expand_loose=expand_loose,
            col=col,
            opacity=opacity,
            tooltip=tooltip,
            visible=visible,
            disabled=disabled,
            data=data,
            rtl=rtl,
        )

        self.key = key
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom
        self.scale = scale
        self.rotate = rotate
        self.offset = offset
        self.aspect_ratio = aspect_ratio
        self.animate_opacity = animate_opacity
        self.animate_size = animate_size
        self.animate_position = animate_position
        self.animate_rotation = animate_rotation
        self.animate_scale = animate_scale
        self.animate_offset = animate_offset
        self.on_animation_end = on_animation_end

    def before_update(self):
        super().before_update()
        self._set_attr_json("rotate", self.__rotate)
        self._set_attr_json("scale", self.__scale)
        self._set_attr_json("offset", self.__offset)
        self._set_attr_json("animateOpacity", self.__animate_opacity)
        self._set_attr_json("animateSize", self.__animate_size)
        self._set_attr_json("animatePosition", self.__animate_position)
        self._set_attr_json("animateRotation", self.__animate_rotation)
        self._set_attr_json("animateScale", self.__animate_scale)
        self._set_attr_json("animateOffset", self.__animate_offset)

    # key
    @property
    def key(self) -> Optional[str]:
        return self._get_attr("key")

    @key.setter
    def key(self, value: Optional[str]):
        self._set_attr("key", value)

    # width
    @property
    def width(self) -> OptionalNumber:
        """
        The width of the control in virtual pixels.
        """
        return self._get_attr("width")

    @width.setter
    def width(self, value: OptionalNumber):
        self._set_attr("width", value)

    # height
    @property
    def height(self) -> OptionalNumber:
        """
        The height of the control in virtual pixels.
        """
        return self._get_attr("height")

    @height.setter
    def height(self, value: OptionalNumber):
        self._set_attr("height", value)

    # left
    @property
    def left(self) -> OptionalNumber:
        """
        The distance that the child's left edge is inset from the left of the stack.

        Effective inside a [`Stack`](/docs/controls/stack) only.
        """
        return self._get_attr("left")

    @left.setter
    def left(self, value: OptionalNumber):
        self._set_attr("left", value)

    # top
    @property
    def top(self) -> OptionalNumber:
        return self._get_attr("top")

    @top.setter
    def top(self, value: OptionalNumber):
        """
        The distance that the child's top edge is inset from the top of the stack.

        Effective inside a [`Stack`](/docs/controls/stack) only.
        """
        self._set_attr("top", value)

    # right
    @property
    def right(self) -> OptionalNumber:
        """
        The distance that the child's right edge is inset from the right of the stack.

        Effective inside a [`Stack`](/docs/controls/stack) only.
        """
        return self._get_attr("right")

    @right.setter
    def right(self, value: OptionalNumber):
        self._set_attr("right", value)

    # bottom
    @property
    def bottom(self) -> OptionalNumber:
        """
        The distance that the child's bottom edge is inset from the bottom of the stack.

        Effective inside a [`Stack`](/docs/controls/stack) only.
        """
        return self._get_attr("bottom")

    @bottom.setter
    def bottom(self, value: OptionalNumber):
        self._set_attr("bottom", value)

    # rotate
    @property
    def rotate(self) -> RotateValue:
        """
        Transforms control using a rotation around the center.

        The value of `rotate` property could be one of the following types:

        * `number` - a rotation in clockwise radians. Full circle `360°` is `math.pi * 2` radians, `90°` is `pi / 2`, `45°` is `pi / 4`, etc.
        * `transform.Rotate` - allows to specify rotation `angle` as well as `alignment` - the location of rotation center.

        For example:

        ```python
        ft.Image(
            src="https://picsum.photos/100/100",
            width=100,
            height=100,
            border_radius=5,
            rotate=Rotate(angle=0.25 * pi, alignment=ft.alignment.center_left)
        )
        ```
        """
        return self.__rotate

    @rotate.setter
    def rotate(self, value: RotateValue):
        self.__rotate = value

    # scale
    @property
    def scale(self) -> ScaleValue:
        """
        Scale control along the 2D plane. Default scale factor is `1.0` - control is not scaled. `0.5` - the control is twice smaller, `2.0` - the control is twice larger.

        Different scale multipliers can be specified for `x` and `y` axis, but setting `Control.scale` property to an instance of `transform.Scale` class:

        ```python
        from dataclasses import field

        class Scale:
            scale: float = field(default=None)
            scale_x: float = field(default=None)
            scale_y: float = field(default=None)
            alignment: Alignment = field(default=None)
        ```

        Either `scale` or `scale_x` and `scale_y` could be specified, but not all of them, for example:

        ```python
        ft.Image(
            src="https://picsum.photos/100/100",
            width=100,
            height=100,
            border_radius=5,
            scale=Scale(scale_x=2, scale_y=0.5)
        )
        ```
        """
        return self.__scale

    @scale.setter
    def scale(self, value: ScaleValue):
        self.__scale = value

    # offset
    @property
    def offset(self) -> OffsetValue:
        """
        Applies a translation transformation before painting the control.

        The translation is expressed as a `transform.Offset` scaled to the control's size. For example, an `Offset` with a `x` of `0.25` will result in a horizontal translation of one quarter the width of the control.

        The following example displays container at `0, 0` top left corner of a stack as transform applies `-1 * 100, -1 * 100` (`offset * control_size`) horizontal and vertical translations to the control:

        ```python
        import flet as ft

        def main(page: ft.Page):

            page.add(
                ft.Stack(
                    [
                        ft.Container(
                            bgcolor="red",
                            width=100,
                            height=100,
                            left=100,
                            top=100,
                            offset=ft.transform.Offset(-1, -1),
                        )
                    ],
                    width=1000,
                    height=1000,
                )
            )

        ft.app(main)
        ```
        """
        return self.__offset

    @offset.setter
    def offset(self, value: OffsetValue):
        self.__offset = value

    # aspect_ratio
    @property
    def aspect_ratio(self) -> OptionalNumber:
        """
        The aspect ratio (width to height) of this control.
        """
        return self._get_attr("aspectRatio")

    @aspect_ratio.setter
    def aspect_ratio(self, value: OptionalNumber):
        self._set_attr("aspectRatio", value)

    # animate_opacity
    @property
    def animate_opacity(self) -> AnimationValue:
        return self.__animate_opacity

    @animate_opacity.setter
    def animate_opacity(self, value: AnimationValue):
        self.__animate_opacity = value

    # animate_size
    @property
    def animate_size(self) -> AnimationValue:
        return self.__animate_size

    @animate_size.setter
    def animate_size(self, value: AnimationValue):
        self.__animate_size = value

    # animate_position
    @property
    def animate_position(self) -> AnimationValue:
        return self.__animate_position

    @animate_position.setter
    def animate_position(self, value: AnimationValue):
        self.__animate_position = value

    # animate_rotation
    @property
    def animate_rotation(self) -> AnimationValue:
        return self.__animate_rotation

    @animate_rotation.setter
    def animate_rotation(self, value: AnimationValue):
        self.__animate_rotation = value

    # animate_scale
    @property
    def animate_scale(self) -> AnimationValue:
        return self.__animate_scale

    @animate_scale.setter
    def animate_scale(self, value: AnimationValue):
        self.__animate_scale = value

    # animate_offset
    @property
    def animate_offset(self) -> AnimationValue:
        return self.__animate_offset

    @animate_offset.setter
    def animate_offset(self, value: AnimationValue):
        self.__animate_offset = value

    # on_animation_end
    @property
    def on_animation_end(self) -> OptionalControlEventCallable:
        return self._get_event_handler("animation_end")

    @on_animation_end.setter
    def on_animation_end(self, handler: OptionalControlEventCallable):
        self._add_event_handler("animation_end", handler)
        self._set_attr("onAnimationEnd", True if handler is not None else None)
