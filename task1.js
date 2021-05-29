var data = {
  rawText: `Расстояние между двумя населенными пунктами 120 км. Автобус преодолевает это расстояние,
  двигаясь со средней скоростью 40 км/ч, а автомобиль - со средней скоростью 60 км/ч.
  На сколько часов пассажиры автобуса находятся в пути дольше, чем пассажиры автомобиля?`,
  actors: [
    {
      id: "uuid-a1",
      name: "actor1",
    },
    {
      id: "uuid-a2",
      name: "actor2",
    }
  ],
  actorModels: [
    {
      id: "uuid-blue-car",
      name: "Машина синяя",
      model: "BLUE_CAR.fbx",
      type: [
        {
          id: "uuid",
          name: "Любой наземный транспорт"
        },
        {
          id: "uuid",
          name: "Любой автомобиль"
        }
      ]
    },
    {
      id: "uuid-blue-bus",
      name: "Автобус синий",
      model: "BLUE_BUS.fbx",
      type: [
        {
          id: "uuid",
          name: "Любой наземный транспорт"
        },
        {
          id: "uuid",
          name: "Любой автомобиль"
        }
      ]
    }
  ],

  world: {
    name: "Земля",
    title: "EARTH",
    dim: 1,

    parameters: [
      {
        name: "g",
        MU: {
          name_short: "Н * м^2/кг^2"
        }
      }
    ],

    model: {
      id: "uuid",
      scene: "ROAD_TWO_WAY",

      type: [
        {
          id: "uuid",
          name: "2 параллели"
        },
        {
          id: "uuid",
          name: "Дорога"
        }
      ]
    }
  },

  motionElements: 
  [
    {
      name: "motion1",

      actor: "uuid-a1",
      model: "uuid-blue-car",

      mainFormulas: [
        {
          formula: "motion1_position_x = motion1_startPosition_x + (time - motion1_startTime) * motion1_velocity * motion1_direction_x",
          parameters: [
            {
              name: "motion1_position_x",
              MU: {
                name_short: "км"
              }
            },
            {
              name: "motion1_startPosition_x",
              MU: {
                name_short: "км"
              }
            },
            {
              name: "time",
              MU: {
                name_short: "ч"
              }
            },
            {
              name: "motion1_startTime",
              MU: {
                name_short: "ч"
              }
            },
            {
              name: "motion1_velocity",
              MU: {
                name_short: "км/ч"
              }
            },
            {
              name: "motion1_direction_x",
              MU: {
                name_short: "vector"
              }
            }
          ]
        }
      ],

      startFormulas: [
        {
          formula: "time = 0",
          parameters: [
            {
              name: "time",
              MU: {
                name_short: "ч"
              }
            }
          ]
        }
      ],

      endFormulas: [
        {
          formula: "motion1_position_x = 120",
          parameters: [
            {
              name: "motion1_position_x",
              MU: {
                name_short: "км"
              }
            }
          ]
        },
      ],

      parameters: [
        {
          name: "motion1_velocity",
          value: 40,
          MU: {
            name_short: "км/ч"
          }
        },
        {
          name: "motion1_startPosition_x",
          value: 0,
          MU: {
            name_short: "км"
          }
        },
        {
          name: "motion1_direction_x",
          value: 1,
        }
      ],
    },
    {
      name: "motion2",

      actor: "uuid-a2",
      model: "uuid-blue-bus",

      mainFormulas: [
        {
          formula: "motion2_position_x = motion2_startPosition_x + (time - motion2_startTime) * motion2_velocity * motion2_direction_x",
          parameters: [
            {
              name: "motion2_position_x",
              MU: {
                name_short: "км"
              }
            },
            {
              name: "motion2_startPosition_x",
              MU: {
                name_short: "км"
              }
            },
            {
              name: "time",
              MU: {
                name_short: "ч"
              }
            },
            {
              name: "motion2_startTime",
              MU: {
                name_short: "ч"
              }
            },
            {
              name: "motion2_velocity",
              MU: {
                name_short: "км/ч"
              }
            },
            {
              name: "motion2_direction_x",
              MU: {
                name_short: "vector"
              }
            }
          ]
        }
      ],

      startFormulas: [
        {
          formula: "time = 0",
          parameters: [
            {
              name: "time",
              MU: {
                name_short: "ч"
              }
            }
          ]
        }
      ],

      endFormulas: [
        {
          formula: "motion2_position_x = 120",
          parameters: [
            {
              name: "motion2_position_x",
              MU: {
                name_short: "км"
              }
            }
          ]
        },
      ],

      parameters: [
        {
          name: "motion2_velocity",
          value: 60,
          MU: {
            name_short: "км/ч"
          }
        },
        {
          name: "motion2_startPosition_x",
          value: 0,
          MU: {
            name_short: "км"
          }
        },
        {
          name: "motion2_direction_x",
          value: 1,
        }
      ],
    }
  ],

  result: {
    paramsToFind: [
      {
        name: "result1",
        MU: {
          name_short: "ч"
        }
      },
    ],

    formulas: {
      formula: "result1 = motion2_time_end - motion1_time_end",
      parameters: [
        {
          name: "result1",
          MU: {
            name_short: "ч"
          }
        },
        {
          name: "motion2_time_end",
          MU: {
            name_short: "ч"
          }
        },
        {
          name: "motion1_time_end",
          MU: {
            name_short: "ч"
          }
        },
      ]
    },
  }
}
