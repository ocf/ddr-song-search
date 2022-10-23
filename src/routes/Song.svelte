<script>
    export let difficulties;
    let {title, subtitle, artist} = difficulties[0]
    console.log(difficulties);
</script>

<div>
{title} by {artist}
</div>

<style>
    div {
        background-color: aliceblue;
        margin: 15px;
	}
</style>
