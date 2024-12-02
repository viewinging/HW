import RPi.GPIO as GPIO
import time

# GPIO 설정
GPIO.setmode(GPIO.BCM)

# 스텝 모터 핀 설정
step_pins = [5, 6, 13, 19]
for pin in step_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

# 스텝 모터 시퀀스 설정
step_sequence = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

# 스텝 모터 동작 함수
def step_motor_with_steps(step_pins, steps, delay):
    """
    스텝 모터를 제어하는 함수
    :param step_pins: 제어할 핀 리스트
    :param steps: 회전할 스텝 수
    :param delay: 각 스텝 간의 지연 시간
    """
    for _ in range(steps):
        for step in step_sequence:
            for pin in range(4):
                GPIO.output(step_pins[pin], step[pin])
            time.sleep(delay)
    for pin in step_pins:
        GPIO.output(pin, False)

try:
    # 예제: 스텝 모터를 180도 회전
    steps_per_revolution = 512  # 360도 회전 스텝 수
    half_revolution = steps_per_revolution // 2  # 180도 회전
    step_motor_with_steps(step_pins, half_revolution, 0.001)

except KeyboardInterrupt:
    print("사용자가 프로그램을 종료했습니다.")

finally:
    # GPIO 핀 초기화
    GPIO.cleanup()
