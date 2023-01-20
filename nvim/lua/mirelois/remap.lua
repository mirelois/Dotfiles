vim.g.mapleader = " "
vim.keymap.set("n", "<leader>pv", vim.cmd.Ex)

--allowes moving selected code
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")

vim.keymap.set("n", "J", "mzJ`z") --change to regular J
--change to regular C-d, C-u
vim.keymap.set("n", "<C-d>", "<C-d>zz")
vim.keymap.set("n", "<C-u>", "<C-u>zz")
--search terms stay in middle search with /
vim.keymap.set("n", "n", "nzzzv")
vim.keymap.set("n", "N", "Nzzzv")

-- greatest remap ever
-- deletes selected text without changing buffer
vim.keymap.set("x", "<leader>p", [["_dP]])

-- next greatest remap ever : asbjornHaland
-- yanks sttuf to clipboard instead of buffer 
vim.keymap.set({ "n", "v" }, "<leader>y", [["+y]])
vim.keymap.set("n", "<leader>Y", [["+Y]])
vim.keymap.set({ "n", "v" }, "<leader>d", [["_d]])

-- This is going to get me cancelled
-- useless for me
vim.keymap.set("i", "<C-c>", "<Esc>")

vim.keymap.set("n", "Q", "<nop>") --disables Q
--dont know what it does exactly--vim.keymap.set("n", "<C-f>", "<cmd>silent !tmux neww tmux-sessionizer<CR>")
vim.keymap.set("n", "<leader>f", vim.lsp.buf.format)--does formating

--quickfix navigation ????
vim.keymap.set("n", "<C-k>", "<cmd>cnext<CR>zz")
vim.keymap.set("n", "<C-j>", "<cmd>cprev<CR>zz")
vim.keymap.set("n", "<leader>k", "<cmd>lnext<CR>zz")
vim.keymap.set("n", "<leader>j", "<cmd>lprev<CR>zz")
--start to replace word you are on
vim.keymap.set("n", "<leader>*", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]])
--start search for current word
vim.keymap.set("n", "<leader>sf", [[yiw:/<C-r>"]])
--makes code executable
vim.keymap.set("n", "<leader>x", "<cmd>!chmod +x %<CR>", { silent = true })
--changing words cycling
vim.keymap.set("n", "<leader><Tab>", "ncw")

--Keymaps for surround
vim.keymap.set("v", [[<leader>(]], [[c(<C-r>")<Esc>]])
vim.keymap.set("v", [[<leader>{]], [[c{<C-r>"}<Esc>]])
vim.keymap.set("v", [[<leader>[]], [[c[<C-r>"]<Esc>]])
vim.keymap.set("v", [[<leader>"]], [[c"<C-r>""<Esc>]])
vim.keymap.set("v", [[<leader>']], [[c'<C-r>"'<Esc>]])

--Keymaps for SQL
vim.keymap.set("n", "<leader>db", ":%DB<CR>")
vim.keymap.set("v", "<leader>db", ":'<,'>DB use mydb; <CR>")
vim.keymap.set("n", "<leader>dbui", ":DBUIToggle<CR>")
vim.keymap.set("n", "<leader>W", "<c-w>w")

