" Artemis-USWDS theme (derived from Rose Pine semantics)

hi clear
" set background=dark
syntax reset

let g:colors_name = "artemis_uswds"

" --- base ---
hi Normal       guifg=None guibg=None
hi CursorLine   guibg=#11151c
hi Visual       guibg=#1a1f2a

" --- text ---
hi Comment      guifg=#71767a gui=italic
hi Constant     guifg=#ffbe2e
"hi String       guifg=#0066b3
hi String		guifg=#f0f0f0
hi Identifier   guifg=#2e7bcf
hi Function     guifg=#f15a29
hi Statement    guifg=#ed1c24
hi Keyword      guifg=#0066b3
hi Type         guifg=#c4a7e7

" --- UI ---
hi LineNr       guifg=#71767a
hi CursorLineNr guifg=#f0f0f0
hi StatusLine   guifg=#f0f0f0 guibg=#11151c
hi VertSplit    guifg=#1a1f2a

" --- diagnostics ---
hi Error        guifg=#e31c3d
hi WarningMsg   guifg=#ffbe2e
hi Todo         guifg=#0b0f14 guibg=#ffbe2e
