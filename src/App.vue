<template>

  <body>
    <section class="relative">
      <div class="
          container
          flex flex-col-reverse
          lg:flex-row
          items-center
          gap-12
          mt-14
          lg:mt-28
        ">
        <div class="flex flex-1 flex-col items-center lg:items-start">
          <h2 class="
              text-5xl
              md:text-4
              lg:text-7xl
              text-center
              lg:text-left
              mb-6
              text-whowflower-limegreen
            ">
            WHOWFlower
          </h2>
          <p class="text-3xl text-center lg:text-left">
            A simple platform to find out WHAT plant or flower you are looking
            at and learn HOW to care for it.
          </p>
          <div class="flex justify-center flex-wrap gap-6">
            <Button btnText="Sign up" class="bg-whowflower-darkgreen text-white hover:bg-white"></Button>
          </div>
        </div>
        <!-- Image -->
        <div class="flex justify-center flex-1 mb-10 md:mb-16 lg:mb-0">
          <img class="
              w-5/6
              h-5/6
              sm:w-3/4 sm:h-3/4
              md:w-5/6 md:h-5/6
              lg:w-full lg:h-full
            " src="./assets/flower.png" style="border-radius: 130px" />
        </div>
        <div></div>
      </div>
    </section>
    <section class="relative">
      <div class="
          container
          flex flex-col-reverse
          lg:flex-row-reverse
          items-center
          gap-12
          mt-14
          mb-14
          lg:mt-28
        ">
        <div id="uploadImageDiv" class="flex-1 flex-col items-center lg:items-start hidden">
          <div class="flex justify-center items-center flex-wrap flex-col">
            <label class="text-center">{{ predictedLabel }}</label>
            <img id="img" src="" class=" h-3/4 w-3/4 mt-5 border-whowflower-limegreen border-4 rounded-md " />
          </div>
        </div>
        <!-- Image upload moet hier -->
        <div class="flex justify-center items-center flex-1 flex-col mb-10 md:mb-16 lg:mb-0">
          <input class="rounded-xl h-0  text-lg mt-5" type="file" id="fileinput" @change="onImageUpload()" />
          <label for="fileinput" id="labelInput"
            class="bg-whowflower-darkgreen overflow-hidden w-1/2 py-2 text-center rounded-md shadow-md text-white lg:text-left">
            <p class="text-center text-2xl"> Upload your image here</p>
          </label>
        </div>
      </div>
    </section>
  </body>
</template>

<script>
import * as tf from '@tensorflow/tfjs';
let test;
export default {
  data() {
    return { predictedLabel: "", model_plant: "" }
  },
  async beforeCreate() {


    test = this.model_plant = await tf.loadLayersModel('src/assets/models/tfjs_flower_model/model.json')
    // tf.loadLayersModel('src/assets/models/tfjs_flower_model/model.json').then((model) => {
    //   this.model_plant = model;
    // this.model_plant.summary();
    // })
  },
  methods: {
    onImageUpload() {
      // add file chec

      this.readURL()

    },
    readURL() {
      let input = document.getElementById("fileinput");

      if (input.files.length < 0) {
        return;
      }

      let uploadImageDiv = document.getElementById("uploadImageDiv");
      uploadImageDiv.classList.remove("hidden");
      uploadImageDiv.classList.add("flex");

      let img = document.getElementById("img");
      // img.setAttribute("height", 200)
      // img.setAttribute("width", 100)

      let filereader = new FileReader();

      let imgTemp = undefined

      // console.log(this.model_plant.summary())
      filereader.onload = function (e) {
        console.log('on load')
        img.src = e.target.result;
        imgTemp = e.target.result
        // console.log(img)

        const a = tf.browser.fromPixels(img, 3).resizeBilinear([120, 200]).div(tf.scalar(255))
        // console.log(a)



        // let fix = tf.concat(resized, 0)
        // console.log(fix)
        a.shape.unshift(1)
        // a.reshape([null, 120, 120, 3])
        a.print()
        // console.log(a)
        let result = test.predict(a)
        console.log("result below kuts")
        let temp = result.dataSync()

        console.log(temp);
        

        
        

        // console.log(result)
        

  
      };


      // this.model_plant.predict(input.files[0])
      // console.log(input.files[0])

      let temp = filereader.readAsDataURL(input.files[0]);


      // im.onload = () => {
      //   const a = tf.browser.fromPixels(im, 4)
      //   a.print()
      //   console.log(a.shape)
      // }

    },
  },
}
</script>