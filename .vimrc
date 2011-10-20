"	|--- VIM creado por Cristian Escudero - 19 Octubre del 2011 ---|
"	|---           Mi .vimrc personal, veamos que sale          ---|

" Basicos {
	
	" Pongo el tipo de encoding como UTF-8
	set enc=utf-8
	set fenc=utf-8
	set termencoding=utf-8

	" No mantengo la compatibilidad con Vi, asi puedo usar todas las 
	" caracteristicas de Vim
	set nocompatible

	" Si un archivo es modificado desde afuera, lo recarga automaticamente
	set autoread

	" Utilizo un esquema de colores que contraste con un fondo oscuro
	set background=dark

	" Esquema de colores slate
	colorscheme las

	" Activamos los colores de sintaxis	
	syntax on

	" Mostramos los numeros de linea
	set number

	" Marca los pares de corchetes, llaves y parentesis
	set showmatch 

	" Crea archivos backup y establezco donde lo guardo
	set backup
	set backupdir=~/.vim/backup
	
	" Pero no creo los archivos de swap
	set noswapfile

	" Hace que el mouse este activo en todo momento, para editar todo
	set mouse=a

	" Me activa un comand line completion al estilo wild
	set wildmenu

	" Ignora esta lista de extensiones
	set wildignore=*.dll,*.o,*.obj,*.bak,*.exe,*pyc,*.jpg,*.gif,*.png

	" Activamos plugins
	filetype plugin on

	" Ponemos el historial en 1000, el default es 20
	set history=1000
	
	" Cuando modificamos el virmc, lo recargamos
	autocmd! bufwritepost vimrc source ~/.vimrc

"	}

" Busqueda {
	
	" Va realizando la busqueda a medidad que se ingresa el texto
	set incsearch
	
	" Busquedas con highlights
	set hls

"	}

" Vim UI  {

	" Hacemos el size del CMD bar de 2
	set cmdheight=2
	
	" Ponemos la regla 
	set ruler
	
	" Y la hacemos mas rosa, no se bien como, pero bueno
	set rulerformat=%30(%=\:b%n%y%m%r%w\ %l,%c%V\ %P%)	

	" Marca con otro color la linea actual
	set cursorline

	" Deja siempre una cantidad de lineas arriba y abajo para scrollear
	set scrolloff=3

	" Hace mas flexible la tecla backspace
	set backspace=indent,eol,start
	set whichwrap+=<,>,h,l

"	}

" Formato de textos y Plantillas {
			
	" Indentacion automatica, manteniendo el mismo nivel que la 
	" identacion anterior
	set autoindent
	
	" Cambio el size de los tabs a 4 espacios
	set tabstop=4

	" Hago busqueda insensitive por default
	set ignorecase
	
	" Evitamos el ajuste de texto
	set nowrap

	" Si hay mayusc en la busqueda, va a Case-Sensitive Search
	set smartcase

	" Corta el texto a los 80 caracteres
	set textwidth=79

	" Comentarios inteligentes
	set comments=sl:/*,mb:\ *,elx:\ */

"	}

" Mapping avanzado de teclas {
	
	""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	" Establecemos un map leader para hacer combinaciones extras de tecla
	" como, <leader>w guarda el archivo
	let mapleader=","
	let g:mapleader=","

	" Una forma de guardar el archivo, con <leader>w
	nmap <leader>w :w!<cr>

	" En modo normal, F2 me guarda el archivo
	nmap <F2> :w!<CR>
	
	" Una forma de ir a editar rapido el vimrc
	nmap <leader>e :e! ~/.vimrc<CR>

	""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	" En modo insertar, F2 me sale del insertar, guarda, y vuelve a entrar
	imap <F2> <ESC>:w!<CR>i

	" Switchea entre header/source con F5 (con extension .hpp y .cpp)
	map <F5> :e %:p:s,.hpp$,.X123X,:s,.cpp$,.hpp,:s,.X123X$,.cpp<CR>

	" Me crea un comentario del tipo Doxygen con F6
	map <F6> :Dox<CR>

	" Es algo super util, :help cope
	map <leader>cc :botright cope<CR>
	map <leader>n :cn<CR>
	map <leader>p :cp<CR>

	""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

	" Me hace el build con F7, y con shift F7
	map <F7> :make<CR>
	map <S-F7> :make clean all<CR>
	
	" Me hace los mapeos, con F3 compilo y con F4 compilo y ejecuto		
	map <F3> : call CompileGcc()<CR>
	func! CompileGcc()
		exec "w"
		exec "!gcc % -o %<"
	endfunc

	map <F4> :call CompileRunGcc()<CR>
	func! CompileRunGcc()
		exec "w"
		exec "!gcc % -o %<"
		exec "! ./%<"
	endfunc

"	}

" Extras {

	" Me configura el Doxygen (si lo tengo instalado)
	let g:DoxygenToolkit_authorName="Cristian Escudero <escudero89@gmail.com>"

"	}
