" Artemis-USWDS Light: NASA Core palette (USWDS + Artemis logo tones)

hi clear
syntax reset

let g:colors_name = "artemis_uswds_light"

" --- base ---
hi Normal       guifg=#000000 guibg=#ffffff
hi CursorLine   guibg=#f5f5f5
hi Visual       guibg=#e8e8e8

" --- syntax ---
hi Comment      guifg=#71767a gui=italic
hi Constant     guifg=#f15a29
hi String       guifg=#000000
hi Identifier   guifg=#000000
hi Function     guifg=#000000
hi Statement    guifg=#ed1c24
hi Keyword      guifg=#ed1c24
hi Type         guifg=#0066b3
hi Special      guifg=#0066b3
hi PreProc      guifg=#0066b3
hi Operator     guifg=#333333

" --- UI ---
hi LineNr       guifg=#71767a
hi CursorLineNr guifg=#000000
hi StatusLine   guifg=#333333 guibg=#f5f5f5
hi VertSplit    guifg=#e8e8e8

" --- diagnostics ---
hi Error        guifg=#e31c3d
hi WarningMsg   guifg=#f15a29
hi Todo         guifg=#ffffff guibg=#f15a29
