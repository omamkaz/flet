from enum import Enum
from typing import Any, Optional, Union

from flet_core import OutlinedBorder
from flet_core.adaptive_control import AdaptiveControl
from flet_core.constrained_control import ConstrainedControl
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import (
    AnimationValue,
    ClipBehavior,
    MarginValue,
    OffsetValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
    OptionalEventCallable,
)


class CardVariant(Enum):
    ELEVATED = "elevated"
    FILLED = "filled"
    OUTLINED = "outlined"


class Card(ConstrainedControl, AdaptiveControl):
    """
    A material design card: a panel with slightly rounded corners and an elevation shadow.

    Example:
    ```
    import flet as ft

    def main(page):
        page.title = "Card Example"
        page.add(
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.ALBUM),
                                title=ft.Text("The Enchanted Nightingale"),
                                subtitle=ft.Text(
                                    "Music by Julie Gable. Lyrics by Sidney Stein."
                                ),
                            ),
                            ft.Row(
                                [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                        ]
                    ),
                    width=400,
                    padding=10,
                )
            )
        )

    ft.app(target=main)

    ```

    -----

    Online docs: https://flet.dev/docs/controls/card
    """

    def __init__(
        self,
        content: Optional[Control] = None,
        margin: MarginValue = None,
        elevation: OptionalNumber = None,
        color: Optional[str] = None,
        shadow_color: Optional[str] = None,
        surface_tint_color: Optional[str] = None,
        shape: Optional[OutlinedBorder] = None,
        clip_behavior: Optional[ClipBehavior] = None,
        is_semantic_container: Optional[bool] = None,
        show_border_on_foreground: Optional[bool] = None,
        variant: Optional[CardVariant] = None,
        #
        # ConstrainedControl and AdaptiveControl
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
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
        key: Optional[str] = None,
        adaptive: Optional[bool] = None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            key=key,
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
            tooltip=tooltip,
            visible=visible,
            disabled=disabled,
            data=data,
        )

        AdaptiveControl.__init__(self, adaptive=adaptive)

        self.content = content
        self.margin = margin
        self.elevation = elevation
        self.color = color
        self.shadow_color = shadow_color
        self.surface_tint_color = surface_tint_color
        self.shape = shape
        self.clip_behavior = clip_behavior
        self.is_semantic_container = is_semantic_container
        self.show_border_on_foreground = show_border_on_foreground
        self.variant = variant

    def _get_control_name(self):
        return "card"

    def before_update(self):
        super().before_update()
        self._set_attr_json("margin", self.__margin)
        self._set_attr_json("shape", self.__shape)

    def _get_children(self):
        children = []
        if self.__content is not None:
            self.__content._set_attr_internal("n", "content")
            children.append(self.__content)
        return children

    # margin
    @property
    def margin(self) -> MarginValue:
        """
        The empty space that surrounds the card.

        Value can be one of the following types: `int`, `float`, or `Margin`.
        """
        return self.__margin

    @margin.setter
    def margin(self, value: MarginValue):
        self.__margin = value

    # elevation
    @property
    def elevation(self) -> OptionalNumber:
        """
        Controls the size of the shadow below the card.

        Defaults to `1.0`. The value must be `None` or a non-negative number.
        """
        return self._get_attr("elevation")

    @elevation.setter
    def elevation(self, value: OptionalNumber):
        self._set_attr("elevation", value)

    # color
    @property
    def color(self) -> Optional[str]:
        """
        The card's background color.

        This is the color used to fill the card's background. Defaults to `None`.
        """
        return self._get_attr("color")

    @color.setter
    def color(self, value: Optional[str]):
        self._set_attr("color", value)

    # shadow_color
    @property
    def shadow_color(self) -> Optional[str]:
        """
        The color of the shadow below the card.

        This color will be used to paint the shadow effect. Defaults to `None`.
        """
        return self._get_attr("shadowColor")

    @shadow_color.setter
    def shadow_color(self, value: Optional[str]):
        self._set_attr("shadowColor", value)

    # surface_tint_color
    @property
    def surface_tint_color(self) -> Optional[str]:
        """
        The color used as an overlay on `color` to indicate elevation.

        If this is `None`, no overlay will be applied. Otherwise, this color will be composited on top of `color` with an opacity related to `elevation` and used to paint the card's background. Defaults to `None`.
        """
        return self._get_attr("surfaceTintColor")

    @surface_tint_color.setter
    def surface_tint_color(self, value: Optional[str]):
        self._set_attr("surfaceTintColor", value)

    # shape
    @property
    def shape(self) -> Optional[OutlinedBorder]:
        """
        The shape of the card.

        Value is of type `OutlinedBorder` and defaults to `RoundedRectangleBorder(radius=4.0)`.
        """
        return self.__shape

    @shape.setter
    def shape(self, value: Optional[OutlinedBorder]):
        self.__shape = value

    # content
    @property
    def content(self) -> Optional[Control]:
        """
        The Control that should be displayed inside the card.

        This control can only have one child. To lay out multiple children, let this control's child be a control such as `Row`, `Column`, or `Stack`, which have a children property, and then provide the children to that control.
        """
        return self.__content

    @content.setter
    def content(self, value: Optional[Control]):
        self.__content = value

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

    # is_semantic_container
    @property
    def is_semantic_container(self) -> bool:
        """
        Set to `True` (default) if this card represents a single semantic container, or `False` if it represents a collection of individual semantic nodes (different types of content).
        """
        return self._get_attr("isSemanticContainer", data_type="bool", def_value=True)

    @is_semantic_container.setter
    def is_semantic_container(self, value: bool):
        self._set_attr("isSemanticContainer", value)

    # show_border_on_foreground
    @property
    def show_border_on_foreground(self) -> bool:
        """
        Whether the shape of the border should be painted in front of the content or behind.

        Defaults to `True`.
        """
        return self._get_attr(
            "showBorderOnForeground", data_type="bool", def_value=True
        )

    @show_border_on_foreground.setter
    def show_border_on_foreground(self, value: bool):
        self._set_attr("showBorderOnForeground", value)

    # variant
    @property
    def variant(self) -> Optional[CardVariant]:
        """
        Defines the card variant to be used.

        Value is of type `CardVariant` and defaults to `CardVariant.ELEVATED`.
        """
        return self.__variant

    @variant.setter
    def variant(self, value: Optional[CardVariant]):
        self.__variant = value
        self._set_enum_attr("variant", value, CardVariant)
