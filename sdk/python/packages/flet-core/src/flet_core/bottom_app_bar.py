from typing import Any, Optional, Union

from flet_core.constrained_control import ConstrainedControl
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import (
    AnimationValue,
    ClipBehavior,
    NotchShape,
    OffsetValue,
    PaddingValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
    OptionalEventCallable,
)


class BottomAppBar(ConstrainedControl):
    """
    A material design bottom app bar.

    -----

    Online docs: https://flet.dev/docs/controls/bottomappbar
    """

    def __init__(
        self,
        content: Optional[Control] = None,
        surface_tint_color: Optional[str] = None,
        bgcolor: Optional[str] = None,
        shadow_color: Optional[str] = None,
        padding: PaddingValue = None,
        clip_behavior: Optional[ClipBehavior] = None,
        shape: Optional[NotchShape] = None,
        notch_margin: OptionalNumber = None,
        elevation: OptionalNumber = None,
        #
        # ConstrainedControl
        #
        ref: Optional[Ref] = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[None, bool, int] = None,
        expand_loose: Optional[bool] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
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
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            width=width,
            height=height,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            expand=expand,
            expand_loose=expand_loose,
            col=col,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            aspect_ratio=aspect_ratio,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            on_animation_end=on_animation_end,
            visible=visible,
            disabled=disabled,
            data=data,
        )

        self.content = content
        self.surface_tint_color = surface_tint_color
        self.bgcolor = bgcolor
        self.shadow_color = shadow_color
        self.padding = padding
        self.shape = shape
        self.clip_behavior = clip_behavior
        self.notch_margin = notch_margin
        self.elevation = elevation

    def _get_control_name(self):
        return "bottomappbar"

    def before_update(self):
        super().before_update()
        self._set_attr_json("padding", self.__padding)

    def _get_children(self):
        if self.__content is not None:
            self.__content._set_attr_internal("n", "content")
            return [self.__content]
        return []

    # content
    @property
    def content(self) -> Optional[Control]:
        """
        A child Control contained by the BottomAppBar.

        This is typically a widget or set of widgets that are displayed within the BottomAppBar.
        """
        return self.__content

    @content.setter
    def content(self, value: Optional[Control]):
        self.__content = value

    # surface_tint_color
    @property
    def surface_tint_color(self) -> Optional[str]:
        """
        The color used as an overlay on `bgcolor` to indicate elevation.

        If this is `None`, no overlay will be applied. Otherwise, this color will be composited on top of `bgcolor` with an opacity related to `elevation` and used to paint the BottomAppBar's background.
        """
        return self._get_attr("surfaceTintColor")

    @surface_tint_color.setter
    def surface_tint_color(self, value: Optional[str]):
        self._set_attr("surfaceTintColor", value)

    # bgcolor
    @property
    def bgcolor(self) -> Optional[str]:
        """
        The fill color to use for the BottomAppBar.

        Default color is defined by the current theme.
        """
        return self._get_attr("bgcolor")

    @bgcolor.setter
    def bgcolor(self, value: Optional[str]):
        self._set_attr("bgcolor", value)

    # shadow_color
    @property
    def shadow_color(self) -> Optional[str]:
        """
        The color of the shadow below the BottomAppBar.
        """
        return self._get_attr("shadowColor")

    @shadow_color.setter
    def shadow_color(self, value: Optional[str]):
        self._set_attr("shadowColor", value)

    # padding
    @property
    def padding(self) -> PaddingValue:
        """
        Empty space to inscribe inside a container decoration (background, border).

        Padding is an instance of the `Padding` class. Defaults to `padding.symmetric(vertical=12.0, horizontal=16.0)`.
        """
        return self.__padding

    @padding.setter
    def padding(self, value: PaddingValue):
        self.__padding = value

    # shape
    @property
    def shape(self) -> Optional[NotchShape]:
        """
        The notch that is made for the floating action button.

        The shape is an instance of the `NotchShape` class.
        """
        return self.__shape

    @shape.setter
    def shape(self, value: Optional[NotchShape]):
        self.__shape = value
        self._set_enum_attr("shape", value, NotchShape)

    # clip_behavior
    @property
    def clip_behavior(self) -> Optional[ClipBehavior]:
        """
        The content will be clipped (or not) according to this option.

        Value is of type `ClipBehavior` and defaults to `ClipBehavior.NONE`.
        """
        return self.__clip_behavior

    @clip_behavior.setter
    def clip_behavior(self, value: Optional[ClipBehavior]):
        self.__clip_behavior = value
        self._set_enum_attr("clipBehavior", value, ClipBehavior)

    # notch_margin
    @property
    def notch_margin(self) -> OptionalNumber:
        """
        The margin between the FloatingActionButton and the BottomAppBar's notch.

        Can be visible only if `shape` is not `None`.
        """
        return self._get_attr("notchMargin")

    @notch_margin.setter
    def notch_margin(self, value: OptionalNumber):
        self._set_attr("notchMargin", value)

    # elevation
    @property
    def elevation(self) -> OptionalNumber:
        """
        This property controls the size of the shadow below the BottomAppBar.

        Defaults to `4`. The value must be `None` or a non-negative number.
        """
        return self._get_attr("elevation")

    @elevation.setter
    def elevation(self, value: OptionalNumber):
        assert value is None or value >= 0, "elevation cannot be negative"
        self._set_attr("elevation", value)
