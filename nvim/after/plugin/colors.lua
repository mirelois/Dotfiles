function Rose_Pine(trans)
    vim.cmd.colorscheme("rose-pine")

    if trans then
        vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
        vim.api.nvim_set_hl(0, "NormalFloat", { bg = "none" })
    end
end

function BOO(_theme,trans)
    require("boo-colorscheme").use({ theme = _theme })

    --themes--
    --sunset_cloud
    --radioactive_waste
    --forest_stream
    --crimson_moonlight

    if trans then
        vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
        vim.api.nvim_set_hl(0, "NormalFloat", { bg = "none" })
    end
end

function TokyoNight(_style,trans)
    require("tokyonight").setup({ style = _style })

    --styles--
    --storm
    --moon
    --night
    --day

    vim.cmd.colorscheme("tokyonight")

    if trans then
        vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
        vim.api.nvim_set_hl(0, "NormalFloat", { bg = "none" })
    end
end

function GruvBox(trans)

    vim.cmd.colorscheme("gruvbox")

    if trans then
        vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
        vim.api.nvim_set_hl(0, "NormalFloat", { bg = "none" })
    end
end

function NightFox(_style,trans)
    require('nightfox').setup({})
    vim.cmd.colorscheme(_style .. "fox")

    --themes--
    --dawn
    --night
    --tera
    --carbon
    --nord
    --dusk
    --day

    if trans then
        vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
        vim.api.nvim_set_hl(0, "NormalFloat", { bg = "none" })
    end
end

function NotColorMyPencils()

    vim.api.nvim_set_hl(0, "Normal", { bg = "black" })
    vim.api.nvim_set_hl(0, "NormalFloat", { bg = "black" })
end

Rose_Pine(1)
