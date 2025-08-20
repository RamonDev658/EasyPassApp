import flet as ft
import string
import random 

def main(page:ft.Page):
  page.theme_mode = ft.ThemeMode.DARK
  page.padding = 0
  page.window.title_bar_hidden = True
  page.window.width = 400
  page.window.min_width = 400
  page.window.height = 700
  page.window.min_height = 700
  
  
  page.theme = ft.Theme(
    color_scheme=ft.ColorScheme(
      primary='#192233',
      on_primary='#ffffff',
      background='#0d121c'
    )
  )
  options={}
  generate_button = ft.Ref[ft.Container]()
  txt_password = ft.Ref[ft.Text]()
  characteres_count = ft.Ref[ft.Slider]()
  btn_clipboard = ft.Ref[ft.IconButton]()
  
  def copy_to_clipboard(e):
    pwd = txt_password.current.value
    
    if pwd:
      page.set_clipboard(pwd)
      btn_clipboard.current.selected = True
      btn_clipboard.update()
      
  
  def toggle_option(e) :
    nonlocal options
    options.update({e.control.data: e.control.value})
    
    if any(options.values()):
      generate_button.current.disabled=False
      generate_button.current.opacity=1
    else:  
      generate_button.current.disabled=True
      generate_button.current.opacity=0.3
      
    generate_button.current.update()  
    
  def generate_password(e):
    pwd = ''
    if options.get('uppercase'):
      pwd += string.ascii_uppercase
    if options.get('lowercase'):
      pwd += string.ascii_lowercase
    if options.get('digits'):
      pwd += string.digits
    if options.get('punctuation'):
      pwd += string.punctuation
      
    count = int(characteres_count.current.value)
    password = random.choices(pwd, k=count)
    txt_password.current.value = ''.join(password)
    txt_password.current.update()
    
    btn_clipboard.current.selected = False
    btn_clipboard.current.update()
    
          
      
  layout = ft.Container(
      expand=True,
       padding=ft.Padding(top=60, left=20, right=20, bottom=20),
      
      gradient=ft.LinearGradient(
        begin=ft.alignment.top_left,
        end=ft.alignment.bottom_right,
        colors=[ft.Colors.PRIMARY, ft.Colors.CYAN]
      ), 
      content=ft.Column(
        scroll=ft.ScrollMode.HIDDEN,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        controls=[
          ft.Text(
            value="Smart Password",
            size=30,
            weight=ft.FontWeight.BOLD,
            text_align= ft.TextAlign.CENTER
          ),
          ft.Divider(height=30, thickness=0.8),
          ft.Container(
             border_radius=ft.border_radius.all(5),
            bgcolor=ft.Colors.with_opacity(0.3,ft.Colors.BLACK),
            content=ft.Row(
              alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
              controls=[
                ft.Text(
                  ref=txt_password,
                  selectable=True,
                  size=20,
                  height=50,
                ),
                ft.IconButton(
                  ref=btn_clipboard,
                  icon=ft.Icons.COPY,
                  icon_color=ft.Colors.WHITE60,
                  selected_icon=ft.Icons.CHECK,
                  selected_icon_color=ft.Colors.BLUE,
                  selected=False,
                  on_click=copy_to_clipboard,
                )
              ]
            )
          ),
          ft.Text(
            value='CARACTERES',
            weight=ft.FontWeight.BOLD,
          ),
          ft.Container(
            bgcolor=ft.Colors.with_opacity(0.8,ft.Colors.BLACK),
            border_radius=ft.border_radius.all(5),
            content=ft.Slider(
              ref=characteres_count,
              value=8,
              min=4,
              max=18,
              divisions=15,
              label='{value}'
              ),
          ),
          ft.Text(
            value='PREFERÊNCIAS',
            weight=ft.FontWeight.BOLD,
          ),
          ft.ListTile(
                    
            title=ft.Text(
              value='Letras Maiúsculas',
              size=16,
            ),
            trailing=ft.Switch(
              active_color=ft.Colors.GREEN_ACCENT_400,
              data='uppercase',
              on_change=toggle_option,
            ),
            toggle_inputs=True,
          ),
          ft.ListTile(
            title=ft.Text(
              value='Letras Minúsculas',
              size=16,
            ),
            trailing=ft.Switch(
              active_color=ft.Colors.GREEN_ACCENT_400,
              data='lowercase',
              on_change=toggle_option,
            ),
            toggle_inputs=True,
          ),
          ft.ListTile(
            title=ft.Text(
              value='Incluir Números',
              size=16,
            ),
            trailing=ft.Switch(
              active_color=ft.Colors.GREEN_ACCENT_400,
              data='digits',
              on_change=toggle_option,
            ),
            toggle_inputs=True,
          ),
          ft.ListTile(
            title=ft.Text(
              value='Incluir Símbolos',
              size=16,
            ),
            trailing=ft.Switch(
              active_color=ft.Colors.GREEN_ACCENT_400,
              data='punctuation',
              on_change=toggle_option,
            ),
            toggle_inputs=True,
          ),
          ft.Container(
            ref=generate_button,
            bgcolor=ft.Colors.with_opacity(0.5,ft.Colors.BLACK),
            border_radius=ft.border_radius.all(5),
            alignment=ft.alignment.center,
            padding=ft.padding.all(20),
            content=ft.Text(
              value="GERAR SENHA",
              weight=ft.FontWeight.BOLD,
            ),
            on_click=generate_password,
            disabled=True,
            opacity=0.3,
            animate_opacity=ft.Animation(duration=700,curve=ft.AnimationCurve.DECELERATE),
          )
          
        ]
      )
  )
  
  page.add(layout)
  
if __name__ == '__main__':
    ft.app(target=main)
