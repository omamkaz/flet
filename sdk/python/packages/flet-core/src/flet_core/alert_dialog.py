from typing import Any, List, Optional

from flet_core.adaptive_control import AdaptiveControl
from flet_core.alignment import Alignment
from flet_core.buttons import OutlinedBorder
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.text_style import TextStyle
from flet_core.types import (
    ClipBehavior,
    MainAxisAlignment,
    PaddingValue,
    OptionalEventCallable,
)


class AlertDialog(AdaptiveControl):
    """
    An alert dialog informs the user about situations that require acknowledgement. An alert dialog has an optional title and an optional list of actions. The title is displayed above the content and the actions are displayed below the content.

    # Example
    ```python
    import flet as ft


    def main(page: ft.Page):
        page.title = "AlertDialog examples"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        dlg = ft.AlertDialog(
            title=ft.Text("Hi, this is a non-modal dialog!"),
            on_dismiss=lambda e: page.add(ft.Text("Non-modal dialog dismissed")),
        )

        def handle_close(e):
            page.close(dlg_modal)
            page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to delete all those files?"),
            actions=[
                ft.TextButton("Yes", on_click=handle_close),
                ft.TextButton("No", on_click=handle_close),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: page.add(
                ft.Text("Modal dialog dismissed"),
            ),
        )

        page.add(
            ft.ElevatedButton("Open dialog", on_click=lambda e: page.open(dlg)),
            ft.ElevatedButton("Open modal dialog", on_click=lambda e: page.open(dlg_modal)),
        )


    ft.app(target=main)
    ```
    -----

    Online docs: https://flet.dev/docs/controls/alertdialog
    """

    def __init__(
        self,
        modal: bool = False,
        title: Optional[Control] = None,
        content: Optional[Control] = None,
        actions: Optional[List[Control]] = None,
        bgcolor: Optional[str] = None,
        elevation: OptionalNumber = None,
        icon: Optional[Control] = None,
        open: bool = False,
        title_padding: PaddingValue = None,
        content_padding: PaddingValue = None,
        actions_padding: PaddingValue = None,
        actions_alignment: Optional[MainAxisAlignment] = None,
        shape: Optional[OutlinedBorder] = None,
        inset_padding: PaddingValue = None,
        icon_padding: PaddingValue = None,
        action_button_padding: PaddingValue = None,
        surface_tint_color: Optional[str] = None,
        shadow_color: Optional[str] = None,
        icon_color: Optional[str] = None,
        scrollable: Optional[bool] = None,
        actions_overflow_button_spacing: OptionalNumber = None,
        alignment: Optional[Alignment] = None,
        content_text_style: Optional[TextStyle] = None,
        title_text_style: Optional[TextStyle] = None,
        clip_behavior: Optional[ClipBehavior] = None,
        semantics_label: Optional[str] = None,
        on_dismiss: OptionalEventCallable = None,
        #
        # AdaptiveControl
        #
        ref: Optional[Ref] = None,
        disabled: Optional[bool] = None,
        visible: Optional[bool] = None,
        data: Any = None,
        adaptive: Optional[bool] = None,
    ):
        Control.__init__(
            self,
            ref=ref,
            disabled=disabled,
            visible=visible,
            data=data,
        )

        AdaptiveControl.__init__(self, adaptive=adaptive)

        self.open = open
        self.bgcolor = bgcolor
        self.elevation = elevation
        self.icon = icon
        self.modal = modal
        self.title = title
        self.title_padding = title_padding
        self.content = content
        self.content_padding = content_padding
        self.actions = actions
        self.actions_padding = actions_padding
        self.actions_alignment = actions_alignment
        self.shape = shape
        self.inset_padding = inset_padding
        self.semantics_label = semantics_label
        self.on_dismiss = on_dismiss
        self.clip_behavior = clip_behavior
        self.action_button_padding = action_button_padding
        self.shadow_color = shadow_color
        self.surface_tint_color = surface_tint_color
        self.icon_padding = icon_padding
        self.icon_color = icon_color
        self.scrollable = scrollable
        self.actions_overflow_button_spacing = actions_overflow_button_spacing
        self.alignment = alignment
        self.content_text_style = content_text_style
        self.title_text_style = title_text_style

    def _get_control_name(self):
        return "alertdialog"

    def before_update(self):
        super().before_update()
        assert (
            self.__title or self.__content or self.__actions
        ), "AlertDialog has nothing to display. Provide at minimum one of the following: title, content, actions"
        self._set_attr_json("actionsPadding", self.__actions_padding)
        self._set_attr_json("contentPadding", self.__content_padding)
        self._set_attr_json("titlePadding", self.__title_padding)
        self._set_attr_json("shape", self.__shape)
        self._set_attr_json("insetPadding", self.__inset_padding)
        self._set_attr_json("iconPadding", self.__icon_padding)
        self._set_attr_json("actionButtonPadding", self.__action_button_padding)
        self._set_attr_json("alignment", self.__alignment)
        if isinstance(self.__content_text_style, TextStyle):
            self._set_attr_json("contentTextStyle", self.__content_text_style)
        if isinstance(self.__title_text_style, TextStyle):
            self._set_attr_json("titleTextStyle", self.__title_text_style)

    def _get_children(self):
        children = []
        if self.__title:
            self.__title._set_attr_internal("n", "title")
            children.append(self.__title)
        if self.__icon:
            self.__icon._set_attr_internal("n", "icon")
            children.append(self.__icon)
        if self.__content:
            self.__content._set_attr_internal("n", "content")
            children.append(self.__content)
        for action in self.__actions:
            action._set_attr_internal("n", "action")
            children.append(action)
        return children

    # open
    @property
    def open(self) -> bool:
        """
        Set to `True` to display a dialog.

        Value is of type `bool` and defaults to `False`.
        """
        return self._get_attr("open", data_type="bool", def_value=False)

    @open.setter
    def open(self, value: Optional[bool]):
        self._set_attr("open", value)

    # bgcolor
    @property
    def bgcolor(self) -> Optional[str]:
        """
        The background [color](/docs/reference/colors) of the dialog's surface.

        Value is of type `str`.
        """
        return self._get_attr("bgcolor")

    @bgcolor.setter
    def bgcolor(self, value: Optional[str]):
        self._set_attr("bgcolor", value)

    # shadow_color
    @property
    def shadow_color(self) -> Optional[str]:
        """
        The [color](/docs/reference/colors) used to paint a drop shadow under the dialog, which reflects the dialog's elevation.

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
        The [color](/docs/reference/colors) used as a surface tint overlay on the dialog's background color, which reflects the dialog's elevation.

        Value is of type `str`.
        """
        return self._get_attr("surfaceTintColor")

    @surface_tint_color.setter
    def surface_tint_color(self, value: Optional[str]):
        self._set_attr("surfaceTintColor", value)

    # icon_color
    @property
    def icon_color(self) -> Optional[str]:
        """
        The [color](/docs/reference/colors) of the icon displayed in the dialog.

        Value is of type `str`.
        """
        return self._get_attr("iconColor")

    @icon_color.setter
    def icon_color(self, value: Optional[str]):
        self._set_attr("iconColor", value)

    # elevation
    @property
    def elevation(self) -> OptionalNumber:
        """
        Defines the elevation (z-coordinate) at which the dialog should appear.

        Value is of type [`OptionalNumber`](/docs/reference/types/aliases#optionalnumber).
        """
        return self._get_attr("elevation", data_type="float")

    @elevation.setter
    def elevation(self, value: OptionalNumber):
        self._set_attr("elevation", value)

    # actions_overflow_button_spacing
    @property
    def actions_overflow_button_spacing(self) -> OptionalNumber:
        """
        Spacing between the action buttons when they overflow.

        Value is of type [`OptionalNumber`](/docs/reference/types/aliases#optionalnumber).
        """
        return self._get_attr("actionsOverflowButtonSpacing", data_type="float")

    @actions_overflow_button_spacing.setter
    def actions_overflow_button_spacing(self, value: OptionalNumber):
        self._set_attr("actionsOverflowButtonSpacing", value)

    # modal
    @property
    def modal(self) -> bool:
        """
        If `True`, the dialog will be modal and block user interaction with other parts of the app.

        Value is of type `bool` and defaults to `False`.
        """
        return self._get_attr("modal", data_type="bool", def_value=False)

    @modal.setter
    def modal(self, value: Optional[bool]):
        self._set_attr("modal", value)

    # title
    @property
    def title(self) -> Optional[Control]:
        """
        Optional title widget for the dialog.

        Value is of type [`Optional[Control]`](/docs/reference/types/aliases#optionalcontrol).
        """
        return self._get_attr("title")

    @title.setter
    def title(self, value: Optional[Control]):
        self._set_attr("title", value)

    # title_padding
    @property
    def title_padding(self) -> PaddingValue:
        """
        Padding around the title widget.

        Value is of type [`PaddingValue`](/docs/reference/types/aliases#paddingvalue) and defaults to `None`.
        """
        return self._get_attr("titlePadding", data_type="padding")

    @title_padding.setter
    def title_padding(self, value: PaddingValue):
        self._set_attr("titlePadding", value)

    # content
    @property
    def content(self) -> Optional[Control]:
        """
        The main content of the dialog.

        Value is of type [`Optional[Control]`](/docs/reference/types/aliases#optionalcontrol).
        """
        return self._get_attr("content")

    @content.setter
    def content(self, value: Optional[Control]):
        self._set_attr("content", value)

    # content_padding
    @property
    def content_padding(self) -> PaddingValue:
        """
        Padding around the content widget.

        Value is of type [`PaddingValue`](/docs/reference/types/aliases#paddingvalue) and defaults to `None`.
        """
        return self._get_attr("contentPadding", data_type="padding")

    @content_padding.setter
    def content_padding(self, value: PaddingValue):
        self._set_attr("contentPadding", value)

    # actions
    @property
    def actions(self) -> Optional[List[Control]]:
        """
        List of actions displayed at the bottom of the dialog.

        Value is of type [`Optional[List[Control]]`](/docs/reference/types/aliases#optionalcontrol).
        """
        return self._get_attr("actions")

    @actions.setter
    def actions(self, value: Optional[List[Control]]):
        self._set_attr("actions", value)

    # actions_padding
    @property
    def actions_padding(self) -> PaddingValue:
        """
        Padding around the actions.

        Value is of type [`PaddingValue`](/docs/reference/types/aliases#paddingvalue) and defaults to `None`.
        """
        return self._get_attr("actionsPadding", data_type="padding")

    @actions_padding.setter
    def actions_padding(self, value: PaddingValue):
        self._set_attr("actionsPadding", value)

    # actions_alignment
    @property
    def actions_alignment(self) -> Optional[MainAxisAlignment]:
        """
        Alignment of the action buttons.

        Value is of type [`Optional[MainAxisAlignment]`](/docs/reference/types/aliases#optionalmainaxisalignment) and defaults to `None`.
        """
        return self._get_attr("actionsAlignment")

    @actions_alignment.setter
    def actions_alignment(self, value: Optional[MainAxisAlignment]):
        self._set_attr("actionsAlignment", value)

    # shape
    @property
    def shape(self) -> Optional[OutlinedBorder]:
        """
        Defines the shape of the dialog's surface.

        Value is of type [`Optional[OutlinedBorder]`](/docs/reference/types/aliases#optionaloutlinedborder) and defaults to `None`.
        """
        return self._get_attr("shape")

    @shape.setter
    def shape(self, value: Optional[OutlinedBorder]):
        self._set_attr("shape", value)

    # inset_padding
    @property
    def inset_padding(self) -> PaddingValue:
        """
        Padding around the dialog's surface, between the dialog and the edge of its parent.

        Value is of type [`PaddingValue`](/docs/reference/types/aliases#paddingvalue) and defaults to `None`.
        """
        return self._get_attr("insetPadding", data_type="padding")

    @inset_padding.setter
    def inset_padding(self, value: PaddingValue):
        self._set_attr("insetPadding", value)

    # icon_padding
    @property
    def icon_padding(self) -> PaddingValue:
        """
        Padding around the icon.

        Value is of type [`PaddingValue`](/docs/reference/types/aliases#paddingvalue) and defaults to `None`.
        """
        return self._get_attr("iconPadding", data_type="padding")

    @icon_padding.setter
    def icon_padding(self, value: PaddingValue):
        self._set_attr("iconPadding", value)

    # action_button_padding
    @property
    def action_button_padding(self) -> PaddingValue:
        """
        Padding around each action button.

        Value is of type [`PaddingValue`](/docs/reference/types/aliases#paddingvalue) and defaults to `None`.
        """
        return self._get_attr("actionButtonPadding", data_type="padding")

    @action_button_padding.setter
    def action_button_padding(self, value: PaddingValue):
        self._set_attr("actionButtonPadding", value)

    # alignment
    @property
    def alignment(self) -> Optional[Alignment]:
        """
        Alignment of the dialog on the screen.

        Value is of type [`Optional[Alignment]`](/docs/reference/types/aliases#optionalalignment) and defaults to `None`.
        """
        return self._get_attr("alignment")

    @alignment.setter
    def alignment(self, value: Optional[Alignment]):
        self._set_attr("alignment", value)

    # content_text_style
    @property
    def content_text_style(self) -> Optional[TextStyle]:
        """
        Text style for the content.

        Value is of type [`Optional[TextStyle]`](/docs/reference/types/aliases#optionaltextstyle) and defaults to `None`.
        """
        return self._get_attr("contentTextStyle")

    @content_text_style.setter
    def content_text_style(self, value: Optional[TextStyle]):
        self._set_attr("contentTextStyle", value)

    # title_text_style
    @property
    def title_text_style(self) -> Optional[TextStyle]:
        """
        Text style for the title.

        Value is of type [`Optional[TextStyle]`](/docs/reference/types/aliases#optionaltextstyle) and defaults to `None`.
        """
        return self._get_attr("titleTextStyle")

    @title_text_style.setter
    def title_text_style(self, value: Optional[TextStyle]):
        self._set_attr("titleTextStyle", value)

    # clip_behavior
    @property
    def clip_behavior(self) -> Optional[ClipBehavior]:
        """
        Determines how the dialog's content is clipped.

        Value is of type [`Optional[ClipBehavior]`](/docs/reference/types/aliases#optionalclipbehavior) and defaults to `None`.
        """
        return self._get_attr("clipBehavior")

    @clip_behavior.setter
    def clip_behavior(self, value: Optional[ClipBehavior]):
        self._set_attr("clipBehavior", value)

    # semantics_label
    @property
    def semantics_label(self) -> Optional[str]:
        """
        Optional label for accessibility purposes.

        Value is of type `str`.
        """
        return self._get_attr("semanticsLabel")

    @semantics_label.setter
    def semantics_label(self, value: Optional[str]):
        self._set_attr("semanticsLabel", value)

    # on_dismiss
    @property
    def on_dismiss(self) -> OptionalEventCallable:
        """
        Callback triggered when the dialog is dismissed.

        Value is of type [`OptionalEventCallable`](/docs/reference/types/aliases#optionaleventcallable).
        """
        return self._get_attr("onDismiss")

    @on_dismiss.setter
    def on_dismiss(self, value: OptionalEventCallable):
        self._set_attr("onDismiss", value)
