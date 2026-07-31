<script>

</script>

<div class="login">
    <span class="rsvp-title">SIGN UP FOR @ NOW!!</span>
    <div class="inner">
        <input class="rsvp" type="text" placeholder="me@hackclub.gay">
        <button class="login-btn">@> </button>
    </div>
</div>

<style>
    .login {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        font-size: var(--font-body);
        font-weight: 500;
    }

    .inner {
        display: flex;
        flex-direction: row;
    }

    .rsvp {
        max-width: 70vw;
        font-size: var(--font-super);
        font-family: monospace;
        font-weight: 800;
        background-color: var(--dimmer);
        border: var(--border-sm) dashed var(--ac);
        border-radius: 1rem 0rem 0rem 1rem;
        text-align: center;
        color: var(--pm);
    }

    @media (width < 600px) {
        .rsvp {
            font-size: var(--font-header);
        }
    }

    .rsvp::placeholder {
        text-align: center;
        font-weight: 400;
    }

    .rsvp:focus {
        border-style: solid;
        outline: none;
    }

    .login-btn {
        border: var(--border-sm) dashed var(--ac);
        border-radius: 0rem 1rem 1rem 0rem;
        border-left: none;
        background-color: var(--dim);
        color: var(--pm);
        font-weight: 1000;
        font-size: var(--font-header);
        transition: 0.1s ease border-color, color;
    }

    .login-btn:hover {
        border-style: solid;
        border-left: none;
    }

    .login-btn:focus {
        border-style: solid;
        border-left: none;
        outline: none;
    }

    .login-btn:active {
        border-color: var(--sc);
        color: var(--sc);
        transition: 0.1s ease border-color;
    }
</style>
