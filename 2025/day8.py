import logging
import sys
from util import parse_args, read_lines, track_time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_input(data):
    return [list(map(int, line.split(','))) for line in data[:-1]], int(data[-1])


def part_1(data, count):
    distances = []
    for i, light1 in enumerate(data):
        for j, light2 in enumerate(data):
            if j <= i:
                continue
            dist = sum((a - b) ** 2 for a, b in zip(light1, light2)) ** 0.5
            distances.append((i, j, dist))
    distances.sort(key=lambda x: x[2])
    logger.debug(f"All distances: {distances}")

    circuits = []
    light_circuit = {}
    for i, j, _ in distances[:count]:
        if i in light_circuit and j in light_circuit:
            circuitIndex1 = light_circuit[i]
            circuitIndex2 = light_circuit[j]
            if circuitIndex1 == circuitIndex2:
                continue
            circuit1 = circuits[circuitIndex1]
            circuit2 = circuits[circuitIndex2]

            for light in circuit2:
                light_circuit[light] = circuitIndex1
            circuit1.update(circuit2)
            circuits[circuitIndex2] = set()
        elif i in light_circuit:
            circuit = circuits[light_circuit[i]]
            circuit.add(j)
            light_circuit[j] = light_circuit[i]
        elif j in light_circuit:
            circuit = circuits[light_circuit[j]]
            circuit.add(i)
            light_circuit[i] = light_circuit[j]
        else:
            light_circuit[i] = len(circuits)
            light_circuit[j] = len(circuits)
            circuits.append({i, j})

    circuits = [c for c in circuits if c]  # Remove empty circuits
    circuits.sort(key=lambda x: -len(x))
    logger.debug(f"Circuits: {circuits}")
    logger.debug(f"Circuit sizes: {[len(c) for c in circuits]}")
    logger.debug(f"Total lights in circuits: {sum(len(c) for c in circuits)}")
    logger.debug(f"Total lights: {len(data)}")

    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])
    




def part_2(data, count):
    distances = []
    for i, light1 in enumerate(data):
        for j, light2 in enumerate(data):
            if j <= i:
                continue
            dist = sum((a - b) ** 2 for a, b in zip(light1, light2)) ** 0.5
            distances.append((i, j, dist))
    distances.sort(key=lambda x: x[2])
    logger.debug(f"All distances: {distances}")

    circuits = []
    light_circuit = {}
    for i, j, _ in distances:
        if i in light_circuit and j in light_circuit:
            circuitIndex1 = light_circuit[i]
            circuitIndex2 = light_circuit[j]
            if circuitIndex1 == circuitIndex2:
                continue
            circuit1 = circuits[circuitIndex1]
            circuit2 = circuits[circuitIndex2]

            for light in circuit2:
                light_circuit[light] = circuitIndex1
            circuit1.update(circuit2)
            circuits[circuitIndex2] = set()
        elif i in light_circuit:
            circuitIndex1 = light_circuit[i]
            circuit = circuits[light_circuit[i]]
            circuit.add(j)
            light_circuit[j] = light_circuit[i]
        elif j in light_circuit:
            circuitIndex1 = light_circuit[j]
            circuit = circuits[light_circuit[j]]
            circuit.add(i)
            light_circuit[i] = light_circuit[j]
        else:
            circuitIndex1 = len(circuits)
            light_circuit[i] = len(circuits)
            light_circuit[j] = len(circuits)
            circuits.append({i, j})
        if len(circuits[circuitIndex1]) == len(data):
            return data[i][0] * data[j][0]

    return 0



if __name__ == "__main__":
    # check all args for verbose flag
    verbose, filename = parse_args(sys.argv)
    if verbose:
        logger.setLevel(logging.DEBUG)
    if filename is None:
        logger.fatal("Missing file name")
        sys.exit(1)

    data = parse_input(read_lines(filename))
    logger.debug(f"Input data: {data}")
    logger.info(f"part 1: {track_time(part_1)(*data)}")
    logger.info(f"part 2: {track_time(part_2)(*data)}")
