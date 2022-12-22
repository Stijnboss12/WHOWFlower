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
            <label class="text-center" id="labeltoupdate">Dit is een {{ predictedLabel }}</label>
            <img id="img" src="./assets/flower.png"
              class=" h-3/4 w-3/4 mt-5 border-whowflower-limegreen border-4 rounded-md " height="120" width="200" />
          </div>
        </div>
        <!-- Image upload moet hier -->
        <div class="flex justify-center items-center flex-1 flex-col mb-10 md:mb-16 lg:mb-0">
          <input class="rounded-xl h-0  text-lg mt-5" type="file" id="fileinput" @change="onImageUpload()" />
          <label for="fileinput" id="labelInput"
            class="bg-whowflower-darkgreen overflow-hidden w-1/2 py-2 text-center rounded-md shadow-md text-white lg:text-left">
            <p class="text-center text-2xl"> Upload your image here</p>

          </label>
          <form class="justify-center items-center flex-1 flex-row mt-5">
            <label for="flowerInput" class="mx-5">Flower</label>
            <input id="flowerInput" type="radio" name="flowerorplant" value="flower" />
            <label for="plantInput" class="mx-5">Plant</label>
            <input id="plantInput" type="radio" name="flowerorplant" value="Plant" />
          </form>
        </div>
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
        <div class="flex flex-1 flex-row items-center lg:items-start">
          <div class="flex flex-1 flex-col m-6 items-start">
            <h2 class="
              text-5xl
              md:text-4
              lg:text-3xl
              text-center
              lg:text-left
              mb-6
              text-whowflower-limegreen
            ">
              This is how to care for your Plant or flower
            </h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
              dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
              ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
              fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
              mollit anim id est laborum.</p>
          </div>
          <div class="flex flex-1 flex-col m-6 items-end">
            <h2 class="
              text-5xl
              md:text-4
              lg:text-3xl
              text-center
              lg:text-left
              mb-6
              text-whowflower-limegreen
            ">
              Do you have any specific questions? Ask them Here!
            </h2>
            <form class="flex flex-col w-11/12 items-end">
              <input class="bg-whowflower-darkgreen rounded-xl border-whowflower-limegreen w-full border-2 mb-6" />
              <button class="bg-whowflower-darkgreen border-whowflower-limegreen border-2 mb-6 rounded-xl w-1/2">Click here to ask!</button>
            </form>
            <h2 class="
              text-5xl
              md:text-4
              lg:text-2xl
              text-center
              lg:text-left
              mb-6
              text-whowflower-limegreen
            ">
              Your answer below...
            </h2>
            <p>Test antwoord</p>
          </div>
        </div>
      </div>
    </section>
  </body>
</template>

<script>
import * as tf from '@tensorflow/tfjs';
import { range } from '@tensorflow/tfjs';
import axios from 'axios'
let test;


export default {
  data() {
    return { predictedLabel: "Loading...", model_plant: "", careGuide: "", question: "", answer: ""}
  },
  async beforeCreate() {


    this.model_flower = await tf.loadLayersModel('src/assets/models/tfjs_flower_model/model.json')
    this.model_plant = await tf.loadLayersModel('src/assets/models/tfjs_plant_model/model.json')
    // tf.loadLayersModel('src/assets/models/tfjs_flower_model/model.json').then((model) => {
    //   this.model_flower = model;
    // this.model_flower.summary();
    // })
  },
  methods: {
    updateVariable(temp) {
      this.predictedLabel = temp
    },
    submitQuestion() {
      
    },
    onImageUpload() {

      let selected = document.querySelector('input[name="flowerorplant"]:checked').value;

      if (selected == 'flower')
        for (let i = 0; i < 2; i++) {
          this.classifyImage(this.model_flower).then((result) => {
            console.log('result')
          })
        }
      else {
        for (let i = 0; i < 2; i++) {
          this.classifyImage(this.model_plant).then((result) => {
            console.log('result')
          })
        }
      }
    },
    async classifyImage(model) {
      console.log(model)
      let input = document.getElementById("fileinput");

      if (input.files.length < 0) {
        return;
      }

      let uploadImageDiv = document.getElementById("uploadImageDiv");

      let img = document.getElementById("img");
      let naturalHeight = img.naturalHeight
      let naturalWidth = img.naturalWidth

      img.setAttribute('height', 120)
      img.setAttribute('width', 200)

      let filereader = new FileReader();

      console.log("Above promise")
      
      const imgResult = new Promise((resolve) => {
        console.log("withing promise")
        filereader.onload = function (e) {
          resolve(e.target.result)
          console.log("Promise resolved")
        }
      })

      filereader.readAsDataURL(input.files[0]);
      console.log("Under promise")

      img.src = await imgResult

      console.log(imgResult)

      console.log("above from pixels")
      console.log(img)
      let tensorImage = await tf.browser.fromPixels(img, 3)
      console.log("above resize")

      let resizedImage = await tensorImage.resizeBilinear([120, 200])
      console.log("above normalize")

      let normalizedImage = await resizedImage.div(tf.scalar(255))

      await normalizedImage.shape.unshift(1)

      // predict
      console.log('NORMASODMOASDMASD')
      normalizedImage.print()
      let pred = model.predict(normalizedImage)
      console.log("Predicition result")
      let predResult = await pred.data()

      const labels = ['Daffodil', 'Dahlia', 'Daisy', 'Dandelion', 'Gerbera', 'Lavender', 'Rose', 'Tulip']

      const maxIndex = predResult.indexOf(Math.max(...predResult));


      console.log(label)

      this.predictedLabel = label;


        // console.log(result)


      uploadImageDiv.classList.add("flex");
      uploadImageDiv.classList.remove("hidden");
    },
  },
}
</script>