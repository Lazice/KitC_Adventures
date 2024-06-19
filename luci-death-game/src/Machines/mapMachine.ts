import {createMachine} from "xstate";

export const mapMachine = createMachine({
  /** @xstate-layout N4IgpgJg5mDOIC5QAoC2BDAxgCwJYDswBKAOgFl0AbSgAgBkwA3MWgRgGIBVABQGUAVAIIBJAEq8A2gAYAuolAAHAPaxcAF1xL88kAA9EAWlYBmAKwljAJgAsADksA2OwHZbrZ6dMAaEAE9DrKyWJA4AnOGhDmZS7qyh1gC+CT5oWHiEpBTU9EwsNBwA4gDyNNyCogDS0nJIIMqqGlo6+ggGjua21sYOMVKmxqGdzj7+rV0kceEOTlLOlja2pkkpGDgExORUtAzMbOzF9MIAQqLlAJrVOvXqmtq1LW3OziTOxq+mMSZu1qYOI4hhEi2KQgyZSSy2ZxSLrLECpNYZTbZHZ5QolADCggAYgBRS61a6NO6gB6OBwTBamVjQ0LOULdf4IIITEHgjyWQbxULg2Hw9IbLLbXJ7UScABy+MUKhuTXuhlpITcIIh0NccWMjKiJGsrKpkWc1g8XUSyThq35mS2OV2+XYWKKdDoRQA6jRREVOHQABqSurSonNRDjHXgnrOVi2KIOWyhRkGcaTfUeD5h5wOXnm9aW5HCmiWdgAERdYoEInEvsJt0DrSC1hI8WMP3mOsNkL+fkMDmeiaexnB1gjDiWpr5WZIvDUACcwGA1LB2EdBOiKjR+CUyIJHRX-VW5UypC8glFTIb3FDXrGO0yPPXWWZqRyobYM2kxxPp7P54vl6v15u6BIrA1FKDS7iSQbkoEpiuGEkRKiYjKOHWrDWO0iyhPMixdi+CIbEcACusA0BO6BEl+S4rmuNAblushXDusrgQglgHuGSFQn00GmDGmrGNquoDr8qHTI2OEWiQBFESRZHsKKEp0QSDHEnohgxhY1i0qYlhmDGMYoYy7jmNyIL3uCtKzM+sL4EoEBwDoo4ZPRoGMSpYwaSQpjhMCrAfIMrDTNYcaWNx-GgieoQ+a4w4rK+iKCtaqJOTKykPEEoQTF5ZiDJCbxDgZrAvKywXRnENjgpZMW4dmQo2pYSUBnuRh9iQxVSFhxksY4caxCyrI9JYTxdFYYljtw6CTgA1vVYGufGMQeeEdJccqtJxuMnlTD0cR0tYAUjYidC4AARpO42jCByXVnNBUbUtHgrcMV6AiG4JmVIfZSFE+0bOi6AAGZgNNLkPDqN1eTEvluAF+WFcqvxuBhOrBd9pDvjOc5Ayl8rkm11LQv5kLvRqV5lSEoIRsCxgxvM6YjpmiKScRaikbc8CKc5WM1oEFiLQ4QTQr8HiPaMgTpcFrxuB495YSjJA4vglDqGA1HoAQNBFH9f24JggPs5de6RB570QuEwURe4jJWHxXRdhG1I+RyrCywAUug+DqEok4AOREeilBKJgE1gJOmPVuMEI+ShHhDp0l6jEYJgkFIEShJ5DgDQOTxJEkQA */
  initial: "Mall Level 1",
  states: {
    "Mall Level 1": {
      on: {
        UPSTAIRS: {
          target: "Mall Level 2",
        },

        "GO PARK": "Park",
        "GO LIBRARY": "Library",
        "GO CAFE": "Cafe",
        RUN: "Bus Stations",
        "FOLLOW ROULX": "Janitor's Clocker"
      },
    },

    "Mall Level 2": {
      on: {
        DOWNSTAIRS: {
          target: "Mall Level 1",
        }
      },
    },

    Park: {},
    Library: {},
    Cafe: {},

    Streets: {
      on: {
        "BACK TO MALL": [{
          target: "Bus Stations",
          guard: "Lost",
        }, "Enlite Main Office"]
      }
    },

    "Bus Stations": {
      on: {
        "BACK TO MALL": "Mall Level 1",
        RUN: "Streets"
      }
    },

    "Enlite Main Office": {},
    "Janitor's Clocker": {}
  },
})