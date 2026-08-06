function love.load()
    player = {}
    player.x = 300
    player.y = 200

    multi = 10
end

function love.update()
    if love.keyboard.isDown('right') then
        player.x = player.x + multi
    end
    if love.keyboard.isDown('left') then
        player.x = player.x - multi
    end
    if love.keyboard.isDown('up') then
        player.y = player.y - multi
    end
    if love.keyboard.isDown('down') then
        player.y = player.y + multi
    end
    
end

function love.draw()
    love.graphics.circle('fill', player.x, player.y, 100)
end