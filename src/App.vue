<template>
  <body>
    <section class="relative">
      <div
        class="
          container
          flex flex-col-reverse
          lg:flex-row
          items-center
          gap-12
          mt-14
          lg:mt-28
        "
      >
        <div class="flex flex-1 flex-col items-center lg:items-start">
          <h2
            class="
              text-5xl
              md:text-4
              lg:text-7xl
              text-center
              lg:text-left
              mb-6
              text-whowflower-limegreen
            "
          >
            WHOWFlower
          </h2>
          <p class="text-3xl text-center lg:text-left">
            A simple platform to find out WHAT plant or flower you are looking
            at and learn HOW to care for it.
          </p>
          <div class="flex justify-center flex-wrap gap-6">
            <Button
              btnText="Sign up"
              class="bg-whowflower-darkgreen text-white hover:bg-white"
            ></Button>
          </div>
        </div>
        <!-- Image -->
        <div class="flex justify-center flex-1 mb-10 md:mb-16 lg:mb-0">
          <img
            class="
              w-5/6
              h-5/6
              sm:w-3/4 sm:h-3/4
              md:w-5/6 md:h-5/6
              lg:w-full lg:h-full
            "
            src="./assets/flower.png"
            style="border-radius: 130px"
          />
        </div>
        <div></div>
      </div>
    </section>
    <section class="relative">
      <div
        class="
          container
          flex flex-col
          lg:flex-row-reverse
          items-center
          gap-12
          mt-14
          mb-14
          lg:mt-28
        "
      >
      <div class="flex flex-1 flex-col items-center lg:items-start">
          <input
            class="rounded-xl text-lg"
            type="file"
            width="48"
            height="48"
            id="fileinput"
            @change="readURL()"
          />
          <img id="img" src="#" alt="your image" class="w-3/4 mt-5" />
          <div class="flex justify-center flex-wrap gap-6">
            <!-- hier moet het resultaat van de image komen -->
          </div>
        </div>
        <!-- Image upload moet hier -->
        <div class="flex justify-center flex-1 mb-10 md:mb-16 lg:mb-0">
          <p
            class="text-3xl text-whowflower-limegreen text-center lg:text-left"
          >
            Upload your image here
          </p>
        </div>
      </div>
    </section>
  </body>
</template>

<script>
export default {
  methods: {
    readURL() {
      let input = document.getElementById("fileinput");

      if (input.files.length < 0) {
        return;
      }

      let img = document.getElementById("img");

      let filereader = new FileReader();

      filereader.onload = function (e) {
        img.src = e.target.result;
      };

      filereader.readAsDataURL(input.files[0]);
    },
  },
};
</script>