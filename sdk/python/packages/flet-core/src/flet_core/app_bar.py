from typing import List, Optional, Any

from flet_core.adaptive_control import AdaptiveControl
from flet_core.buttons import OutlinedBorder
from flet_core.control import Control
from flet_core.ref import Ref
from flet_core.text_style import TextStyle
from flet_core.types import ClipBehavior, OptionalNumber


class AppBar(AdaptiveControl):
    """
    A material design app bar.

    Example:
    ```
    import flet as ft

    def main(page: ft.Page):
        def check_item_clicked(e):
            e.control.checked = not e.control.checked
            page.update()

        page.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.PALETTE),
            leading_width=40,
            title=ft.Text("AppBar Example"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
                ft.IconButton(ft.icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            text="Checked item", checked=False, on_click=check_item_clicked
                        ),
                    ]
                ),
            ],
        )
        page.add(ft.Text("Body!"))

    ft.app(target=main)

    ```

    -----

    Online docs: https://flet.dev/docs/controls/appbar
    """

    def __init__(
        self,
        leading: Optional[Control] = None,
        leading_width: OptionalNumber = None,
        automatically_imply_leading: Optional[bool] = None,
        title: Optional[Control] = None,
        center_title: Optional[bool] = None,
        toolbar_height: OptionalNumber = None,
        color: Optional[str] = None,
        bgcolor: Optional[str] = None,
        elevation: OptionalNumber = None,
        elevation_on_scroll: OptionalNumber = None,
        shadow_color: Optional[str] = None,
        surface_tint_color: Optional[str] = None,
        clip_behavior: Optional[ClipBehavior] = None,
        force_material_transparency: Optional[bool] = None,
        is_secondary: Optional[bool] = None,
        title_spacing: OptionalNumber = None,
        exclude_header_semantics: Optional[bool] = None,
        actions: Optional[List[Control]] = None,
        toolbar_opacity: OptionalNumber = None,
        title_text_style: Optional[TextStyle] = None,
        toolbar_text_style: Optional[TextStyle] = None,
        shape: Optional[OutlinedBorder] = None,
        #
        # AdaptiveControl
        #
        ref: Optional[Ref] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
        adaptive: Optional[bool] = None,
    ):
        Control.__init__(self, ref=ref, visible=visible, disabled=disabled, data=data)

        AdaptiveControl.__init__(self, adaptive=adaptive)

        self.leading = leading
        self.leading_width = leading_width
        self.automatically_imply_leading = automatically_imply_leading
        self.title = title
        self.center_title = center_title
        self.toolbar_height = toolbar_height
        self.color = color
        self.bgcolor = bgcolor
        self.elevation = elevation
        self.actions = actions
        self.elevation_on_scroll = elevation_on_scroll
        self.shadow_color = shadow_color
        self.surface_tint_color = surface_tint_color
        self.clip_behavior = clip_behavior
        self.force_material_transparency = force_material_transparency
        self.is_secondary = is_secondary
        self.title_spacing = title_spacing
        self.exclude_header_semantics = exclude_header_semantics
        self.toolbar_opacity = toolbar_opacity
        self.title_text_style = title_text_style
        self.toolbar_text_style = toolbar_text_style
        self.shape = shape

    def _get_control_name(self):
        return "appbar"

    def before_update(self):
        super().before_update()
        if isinstance(self.__title_text_style, TextStyle):
            self._set_attr_json("titleTextStyle", self.__title_text_style)
        if isinstance(self.__toolbar_text_style, TextStyle):
            self._set_attr_json("toolbarTextStyle", self.__toolbar_text_style)
        if isinstance(self.__shape, OutlinedBorder):
            self._set_attr_json("shape", self.__shape)

    def _get_children(self):
        children = []
        if self.__leading:
            self.__leading._set_attr_internal("n", "leading")
            children.append(self.__leading)
        if self.__title:
            self.__title._set_attr_internal("n", "title")
            children.append(self.__title)
        for action in self.__actions:
            action._set_attr_internal("n", "action")
            children.append(action)
        return children

    # leading
    @property
    def leading(self) -> Optional[Control]:
        """
        A `Control` to display before the toolbar's title.

        Typically the leading control is an [`Icon`](/docs/controls/icon) or an [`IconButton`](/docs/controls/iconbutton).
        """
        return self.__leading

    @leading.setter
    def leading(self, value: Optional[Control]):
        self.__leading = value

    # leading_width
    @property
    def leading_width(self) -> OptionalNumber:
        """
        Defines the width of the leading control.

        Value is of type [`OptionalNumber`](/docs/reference/types/aliases#optionalnumber) and defaults to `56.0`.
        """
        return self._get_attr("leadingWidth")

    @leading_width.setter
    def leading_width(self, value: OptionalNumber):
        self._set_attr("leadingWidth", value)

    # title_spacing
    @property
    def title_spacing(self) -> OptionalNumber:
        """
        The spacing around the `title` on the horizontal axis. It is applied even if there are no `leading` or `actions` controls.

        If you want `title` to take all the space available, set this value to `0.0`.

        Value is of type [`OptionalNumber`](/docs/reference/types/aliases#optionalnumber).
        """
        return self._get_attr("titleSpacing", data_type="float")

    @title_spacing.setter
    def title_spacing(self, value: OptionalNumber):
        self._set_attr("titleSpacing", value)

    # toolbar_opacity
    @property
    def toolbar_opacity(self) -> float:
        """
        The opacity of the toolbar. Value ranges from `0.0` (transparent) to `1.0` (fully opaque).

        Value is of type [`OptionalNumber`](/docs/reference/types/aliases#optionalnumber) and defaults to `1.0`.
        """
        return self._get_attr("toolbarOpacity", data_type="float", def_value=1.0)

    @toolbar_opacity.setter
    def toolbar_opacity(self, value: OptionalNumber):
        assert value is None or (
            0 >= value >= 1
        ), "toolbar_opacity is out of range (0-1)"
        self._set_attr("toolbarOpacity", value)

    # shape
    @property
    def shape(self) -> Optional[OutlinedBorder]:
        """
        The shape of the app bar's Material as well as its shadow.

        Value is of type [`OutlinedBorder`](/docs/reference/types/outlinedborder).
        """
        return self.__shape

    @shape.setter
    def shape(self, value: Optional[OutlinedBorder]):
        self.__shape = value

    # title_text_style
    @property
    def title_text_style(self) -> Optional[TextStyle]:
        """
        The style to be used for the `Text` controls in the `title`.

        Value is of type [`TextStyle`](/docs/reference/types/textstyle).
        """
        return self.__title_text_style

    @title_text_style.setter
    def title_text_style(self, value: Optional[TextStyle]):
        self.__title_text_style = value

    # toolbar_text_style
    @property
    def toolbar_text_style(self) -> Optional[TextStyle]:
        """
        The style to be used for the `Text` controls in the app bar's `leading` and `actions` (but not `title`).

        Value is of type [`TextStyle`](/docs/reference/types/textstyle).
        """
        return self.__toolbar_text_style

    @toolbar_text_style.setter
    def toolbar_text_style(self, value: Optional[TextStyle]):
        self.__toolbar_text_style = value

    # automatically_imply_leading
    @property
    def automatically_imply_leading(self) -> bool:
        """
        Controls whether the leading widget should be implied if `leading` is `None`.

        If `True` and `leading` is `None`, the system will automatically try to deduce what the leading widget should be. If `False` and `leading` is `None`, the leading space is given to the title. If a leading widget is provided, this parameter has no effect.

        Value is of type `bool`.
        """
        return self._get_attr(
            "automaticallyImplyLeading", data_type="bool", def_value=True
        )

    @automatically_imply_leading.setter
    def automatically_imply_leading(self, value: Optional[bool]):
        self._set_attr("automaticallyImplyLeading", value)

    # title
    @property
    def title(self) -> Optional[Control]:
        """
        The primary widget displayed in the app bar, typically a `Text` widget.

        The title is placed between the `leading` and `actions` widgets.
        """
        return self.__title

    @title.setter
    def title(self, value: Optional[Control]):
        self.__title = value

    # center_title
    @property
    def center_title(self) -> bool:
        """
        Whether the `title` is centered.

        If set to `True`, the `title` widget will be centered within the app bar. Otherwise, the `title` will align to the start of the space between `leading` and `actions`.

        Value is of type `bool`.
        """
        return self._get_attr("centerTitle", data_type="bool", def_value=False)

    @center_title.setter
    def center_title(self, value: Optional[bool]):
        self._set_attr("centerTitle", value)

    # toolbar_height
    @property
    def toolbar_height(self) -> OptionalNumber:
        """
        The height of the toolbar.

        Value is of type [`OptionalNumber`](/docs/reference/types/aliases#optionalnumber).
        """
        return self._get_attr("toolbarHeight", data_type="float")

    @toolbar_height.setter
    def toolbar_height(self, value: OptionalNumber):
        self._set_attr("toolbarHeight", value)

    # color
    @property
    def color(self) -> Optional[str]:
        """
        The foreground color to be used within the app bar, typically applied to text and iconography.

        Value is of type `str`.
        """
        return self._get_attr("color")

    @color.setter
    def color(self, value: Optional[str]):
        self._set_attr("color", value)

    # bgcolor
    @property
    def bgcolor(self) -> Optional[str]:
        """
        The background color of the app bar.

        Value is of type `str`.
        """
        return self._get_attr("bgcolor")

    @bgcolor.setter
    def bgcolor(self, value: Optional[str]):
        self._set_attr("bgcolor", value)

    # elevation
    @property
    def elevation(self) -> OptionalNumber:
        """
        The z-coordinate at which to place this app bar. This controls the size of the shadow below the app bar.

        Value is of type [`OptionalNumber`](/docs/reference/types/aliases#optionalnumber).
        """
        return self._get_attr("elevation", data_type="float")

    @elevation.setter
    def elevation(self, value: OptionalNumber):
        self._set_attr("elevation", value)

    # elevation_on_scroll
    @property
    def elevation_on_scroll(self) -> OptionalNumber:
        """
        The elevation to be applied to the app bar when the user scrolls up.

        Value is of type [`OptionalNumber`](/docs/reference/types/aliases#optionalnumber).
        """
        return self._get_attr("elevationOnScroll", data_type="float")

    @elevation_on_scroll.setter
    def elevation_on_scroll(self, value: OptionalNumber):
        self._set_attr("elevationOnScroll", value)

    # shadow_color
    @property
    def shadow_color(self) -> Optional[str]:
        """
        The color of the shadow below the app bar.

        Value is of type `str`.
        """
        return self._get_attr("shadowColor")

    @shadow_color.setter
    def shadow_color(self, value: Optional[str]):
        self._set_attr("shadowColor", value)

    # surface_tint_color
    @property
    def surface_tint_color(self) -> Optional[str]:
        """
        The color used as an overlay on the app bar when it has a background color.

        Value is of type `str`.
        """
        return self._get_attr("surfaceTintColor")

    @surface_tint_color.setter
    def surface_tint_color(self, value: Optional[str]):
        self._set_attr("surfaceTintColor", value)

    # clip_behavior
    @property
    def clip_behavior(self) -> Optional[ClipBehavior]:
        """
        The content of the app bar will be clipped (or not) according to this option.

        Value is of type [`ClipBehavior`](/docs/reference/types/clipbehavior).
        """
        return self._get_attr("clipBehavior")

    @clip_behavior.setter
    def clip_behavior(self, value: Optional[ClipBehavior]):
        self._set_attr("clipBehavior", value)

    # force_material_transparency
    @property
    def force_material_transparency(self) -> Optional[bool]:
        """
        Forces the app bar to use a material design with transparent background, even if it is not secondary.

        Value is of type `bool`.
        """
        return self._get_attr("forceMaterialTransparency", data_type="bool")

    @force_material_transparency.setter
    def force_material_transparency(self, value: Optional[bool]):
        self._set_attr("forceMaterialTransparency", value)

    # is_secondary
    @property
    def is_secondary(self) -> Optional[bool]:
        """
        Indicates whether the app bar is a secondary app bar.

        Value is of type `bool`.
        """
        return self._get_attr("isSecondary", data_type="bool")

    @is_secondary.setter
    def is_secondary(self, value: Optional[bool]):
        self._set_attr("isSecondary", value)

    # exclude_header_semantics
    @property
    def exclude_header_semantics(self) -> Optional[bool]:
        """
        Whether to exclude the app bar's header semantics from the overall app bar semantics.

        Value is of type `bool`.
        """
        return self._get_attr("excludeHeaderSemantics", data_type="bool")

    @exclude_header_semantics.setter
    def exclude_header_semantics(self, value: Optional[bool]):
        self._set_attr("excludeHeaderSemantics", value)

    # actions
    @property
    def actions(self) -> Optional[List[Control]]:
        """
        A list of `Control` objects displayed on the right side of the app bar.

        Typically these controls are icons or buttons for various actions.
        """
        return self.__actions

    @actions.setter
    def actions(self, value: Optional[List[Control]]):
        self.__actions = value
