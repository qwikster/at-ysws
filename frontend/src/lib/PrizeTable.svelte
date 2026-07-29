<script>

</script>

<div class="tiles">
    <div class="tile">
        <span class="tile-head">HTTP</span>
        <div class="tile-body">
            <div class="tile-part">
                <div class="tile-l"> YS </div>
                <div class="tile-r">
                    <span class="item"><at>@</at> new Requests library</span>
                    <span class="item"><at>@</at> HTTP client or server</span>
                    <span class="item"><at>@</at> custom HTTP router</span>
                    <span>meow</span>
                </div>
            </div>
            <div class="tile-part">
                <div class="tile-l tlb"> WS </div>
                <div class="tile-r">
                    <span class="item"><at>@</at> domain grant [3h]</span>
                </div>
            </div>
        </div>
    </div>
    <div class="tile">
        <span class="tile-head">TCP/IP</span>
        <div class="tile-body">
            <div class="tile-part">
                <div class="tile-l"> YS </div>
                <div class="tile-r">
                    <span class="item"><at>@</at> JSON chat app</span>
                    <span class="item"><at>@</at> new protocol atop TCP</span>
                </div>
            </div>
            <div class="tile-part">
                <div class="tile-l tlb"> WS </div>
                <div class="tile-r">
                    <span class="item"><at>@</at> Ethernet patch cables [2h]</span>
                    <span class="item"><at>@</at> Raspberry Pi Zero 2 W [10h]</span>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .tiles {
        display: flex;
        flex-wrap: wrap;
        width: 100%;
        gap: var(--gap-l);
        margin-top: var(--pad-v);
    }

    .tile {
        display: flex;
        flex-grow: 1;
        white-space: nowrap;
        flex-direction: column;
        border: var(--border-sm) solid var(--ac);
        border-radius: 1rem;
    }

    .tile-body {
        font-size: var(--font-body);
        display: flex;
        flex-direction: column;
        flex-grow: 1;
    }

    .tile-part {
        display: flex;
        flex-direction: row;
    }

    .tile-part:last-child {
        flex-grow: 1;
    }

    .tile-head {
        text-align: center;
        font-weight: 800;
        font-size: var(--font-header);

        border-radius: 0.8rem 0.8rem 0px 0px;
        border-bottom: 0.2rem dashed var(--fg);

        background: repeating-linear-gradient(
          -45deg,
          var(--dim),
          var(--dim) 10px,
          var(--dimmer) 10px,
          var(--dimmer) 20px
        );
    }

    .tile-part:first-child {
        border-bottom: 0.2rem dashed var(--fg);
    }

    .tile-l {
        display: flex;
        align-items: center;
        border-right: 0.2rem dashed var(--fg);
        padding: 0rem 0.3rem 0rem 0.2rem;
        font-weight: 500;
        color: var(--sc);
        text-shadow: 1px 1px 2px var(--sc);
        background-color: rgb(from var(--dim) r g b / 50%);
    }

    .tlb {
        border-bottom-left-radius: 0.8rem;
    }

    .tile-r {
        padding: 0.2rem 0rem 0.2rem 0.4rem;
    }

    .item {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 0.4rem;
    }
</style>
