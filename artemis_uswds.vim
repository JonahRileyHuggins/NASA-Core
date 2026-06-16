" Artemis-USWDS: NASA Core palette (USWDS + Artemis logo tones)

hi clear
syntax reset

let g:colors_name = "artemis_uswds"

" --- base ---
hi Normal       guifg=#ffffff guibg=#0b0f14
hi CursorLine   guibg=#11151c
hi Visual       guibg=#1a1f2a

" --- syntax ---
hi Comment      guifg=#71767a gui=italic
hi Constant     guifg=#f15a29
hi String       guifg=#ffffff
hi Identifier   guifg=#ffffff
hi Function     guifg=#ffffff
hi Statement    guifg=#ed1c24
hi Keyword      guifg=#ed1c24
hi Type         guifg=#0066b3
hi Special      guifg=#0066b3
hi PreProc      guifg=#0066b3
hi Operator     guifg=#f0f0f0

" --- UI ---
hi LineNr       guifg=#71767a
hi CursorLineNr guifg=#ffffff
hi StatusLine   guifg=#f0f0f0 guibg=#11151c
hi VertSplit    guifg=#1a1f2a

" --- diagnostics ---
hi Error        guifg=#e31c3d
hi WarningMsg   guifg=#f15a29
hi Todo         guifg=#0b0f14 guibg=#f15a29
