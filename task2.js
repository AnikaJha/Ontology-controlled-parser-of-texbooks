var data = {
  rawText: `Самолет пролетает 100 км за 5 мин. Определите скорость самолета в м/с и км/ч.`,
  actors: [
    {
      id: "Актор_4e4fac1e-8ebe-4729-86f4-bfe5a4e9a8f6",
      name: "actor1",
    }
  ],
  actorModels: [
    {
      id: "АкторModel_347a69d1-d5ef-420c-9420-570c3bf93b18",
      name: "Синий самолет",
      model: "BLUE_PLANE.fbx",
      type: [
        {
          id: "uuid",
          name: "Любой самолет"
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
      scene: "SKY",

      type: [
        {
          id: "uuid",
          name: "1 параллель"
        },
        {
          id: "uuid",
          name: "Воздушное пространство"
        }
      ]
    }
  },

  motionElements: 
  [
    {
      name: "motion1",

      actor: "Актор_4e4fac1e-8ebe-4729-86f4-bfe5a4e9a8f6",
      model: "АкторModel_347a69d1-d5ef-420c-9420-570c3bf93b18",

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
          formula: "motion1_position_x = 100",
          parameters: [
            {
              name: "motion1_position_x",
              MU: {
                name_short: "км"
              }
            }
          ]
        },
        {
          formula: "time = 5",
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

      parameters: [
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
    }
  ],

  result: {
    paramsToFind: [
      {
        name: "motion1_velocity",
        MU: {
          name_short: "м/c"
        }
      },
      {
        name: "motion1_velocity",
        MU: {
          name_short: "км/ч"
        }
      }
    ]
  }
}
